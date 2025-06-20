Here’s a **comprehensive deep-dive breakdown** of the Facebook Post Search design, aligned with what a **staff-level engineer** would be expected to handle during a system design interview.

---

## 🔍 **Deep Dive Areas**

We'll go step by step into:

1. **Inverted Index**
2. **Search Query Optimization (likes + recency sort)**
3. **Write Path Scalability**
4. **Redis Scaling + Sharding**
5. **Hot vs Cold Indexing (Eviction Strategy)**
6. **Like Count Approximation (Log Scale + Batching)**
7. **Handling Multi-Word (Bi-gram/N-gram) Queries**

---

### 1. 🧠 Inverted Index

**Definition:**
A map from `keyword → sorted list of postIds`.

**Write Path (Index Construction):**

* On post creation, tokenize the post.
* For each token, insert postId into:

  * `time:<keyword>` sorted set → scored by timestamp.
  * `like:<keyword>` sorted set → scored by like count/log(like).

**Read Path:**

* Query `time:<keyword>` or `like:<keyword>`, sorted by requested order.

**Optimizations:**

* Use **Redis sorted sets (ZSET)** to support fast ranked retrieval.
* Use **stopword filtering + stemming** to reduce index bloat.

**Reasoning:**

* Fast lookup by keyword.
* Sortability enables instant “top N” results without rescanning.

---

### 2. ⏱️ Search Query Optimization (Sort by Likes/Recency)

**Challenge:**

* One inverted index can’t support two sort orders.

**Solution:**

* Create **two separate indexes** per keyword:

  * `time:<keyword>` (sorted by post timestamp)
  * `like:<keyword>` (sorted by like count/log scale)

**Final Sorting Step:**

* Optional rescoring (e.g., fetch actual like counts for top 50 posts).
* Enables **approximated pre-sorting + accurate top-N** ranking.

**Why not always sort in search service?**

* Too many IDs = high latency, bandwidth hit (10M postIds ≈ 100MB).
* Sorting in Redis with ZSET reduces payload drastically.

---

### 3. 🔁 Write Path Scalability (Post + Like Ingestion)

**Volume:**

* 10K posts/sec, 100K likes/sec (write-heavy system).

**Strategy:**

* Use **Kafka as buffer** between:

  * Post DB → Ingestion Service
  * Likes Count Cache → Ingestion Service

**Benefits:**

* Async, fault-tolerant.
* Replayable (via offset tracking).
* Backpressure support in ingestion spikes.

**Alternative to Kafka:**

* Debezium (for CDC) → Kafka → Flink/Consumer Pipeline.

---

### 4. 🧱 Redis Scaling and Sharding Strategy

**Single-node Redis Limitations:**

* 100K ops/sec per core/node.
* Memory-bound, single-threaded per shard.

**Sharding Options:**

1. **By keyword**

   * Simple but hot-key risk (e.g., “TaylorSwift” blows up one node).

2. **By keyword + postId mod N**

   * `like:<keyword>:shard_1`, `shard_2`… balances hot keys.

**Trade-off:**

* More shards = better write distribution.
* But read path (search service) must merge across multiple shards.

**Solution:**

* Use **sorted-merge strategy** in search service (like K-way merge).
* Cache top N result sets per shard to reduce repeated lookups.

---

### 5. 🔥 Hot vs ❄️ Cold Indexing (Storage Eviction Strategy)

**Problem:**

* Billions of keywords lead to RAM pressure on Redis.

**Solution:**

* Evict low-read/low-write keywords to S3 (cold storage).

**Eviction Policy:**

* Use **Count-Min Sketch** to estimate:

  * Search frequency
  * Ingestion frequency

**Flow:**

* If `frequency(keyword) < threshold`, evict to cold.
* On cache miss → search service checks cold index (fallback path).
* Background job can re-promote keywords if they get hot again.

---

### 6. 📉 Like Count Approximation (Logarithmic Scoring + Batching)

**Problem:**

* Updating like count in ZSET for every event = 100K writes/sec.

**Approach A: Log-Scale Compression**

* Store `log2(likeCount)` as score in Redis.
* Only update when `log2(newCount) > log2(oldCount)`.
* Reduces writes drastically — e.g., 64→65 does nothing until 128.

**Approach B: Batch Updates**

* Collect like events in Flink or a custom batcher.
* Emit deltas every N seconds (e.g., 30s).
* Merge into search index.

**Combined Strategy:**

* Log-scale + batching + final rescoring in search service → best of all worlds.

---

### 7. 🧩 Multi-Word (Bi-gram / N-gram) Search

**Challenge:**

* "Taylor Swift" should not match "Taylor danced by the Swift River".

**Options:**

1. **On-demand Filtering**:

   * Intersect results from `Taylor` and `Swift`, then check adjacency from DB.
   * Accurate but slow.

2. **Precomputed Bi-gram Indexing**:

   * Index 2-word pairs (e.g., "Taylor Swift", "Swift River").
   * Increases index size \~2x–3x.

3. **Evict Rare Bi-grams**:

   * Use Count-Min Sketch to keep only frequently searched bi-grams.

**Trade-offs:**

* **Precision vs space**.
* Popular queries like "World Cup" deserve dedicated bi-gram entries.

---

## 🔁 Summary Table

| Area                  | Strategy                                                                |
| --------------------- | ----------------------------------------------------------------------- |
| Inverted Index        | Redis Sorted Set per keyword per sort mode (time, like)                 |
| Search Sorting        | Use separate indexes; avoid real-time sorting of huge lists             |
| Write Scalability     | Kafka + Stateless Ingestion + CDC + Batching                            |
| Redis Scaling         | Keyword sharding + postId mod N (sharded sorted sets)                   |
| Like Volume Reduction | Logarithmic scoring + Flink batching                                    |
| Memory Optimization   | Cold index eviction via Count-Min Sketch                                |
| Multi-word Queries    | Intersection + filtering or Bi-gram indexing w/ frequency-based storage |

---

Would you like a visual version of this architecture now (with arrows, boxes, etc.) or a formatted PDF-style cheat sheet to study from?
