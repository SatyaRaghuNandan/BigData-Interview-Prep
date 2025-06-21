Facebook Post Search System Design
Inverted Index Optimization
To optimize searches, we arrange data for fast reads, similar to an inverted index. Ideally, the list of post IDs for a keyword is pre-sorted by creation time, allowing the search service to fetch the top 100 items without additional sorting. However, we support two sort orders: creation time and like count. A single sort order cannot satisfy both, so we create two indexes per keyword: one for likes and one for time. Using Redis sorted sets, we store post IDs with scores based on like count or timestamp. This enables O(log n) queries. The search service selects the appropriate index (e.g., likes:{keyword} or time:{keyword}) and retrieves the top N items. We cap sorted sets at the top 100 post IDs per keyword to manage storage, focusing on high-engagement or recent posts.
Like Event Handling
To maintain these indexes, the like service notifies the ingestion service of like events. Previously, likes wrote directly to the search index, which was inefficient. Instead, we store likes in a Likes DB and maintain a volatile Redis cache for like counts (e.g., post:{id}:likes). When a like or unlike occurs, we increment/decrement the cache and write to the Likes DB. Like count changes are sent to a Kafka topic (like-events) via CDC, ensuring fault tolerance. The ingestion service consumes these events, retrieves the post content, tokenizes it, and updates the relevant Redis sorted sets. This process is write-heavy, as like events are frequent, creating a potential bottleneck.
Functional Requirements
This design meets functional requirements: users can search by keyword with sorting by time or likes. The system functions but requires optimization to address non-functional requirements like latency and throughput.
Deep Dives
1. Low Latency and High Read Throughput
Challenge: High read volume (e.g., many users searching for "Taylor Swift" after a news event) strains the search service and Redis indexes.Solution:  

External Cache: Use a Redis cache to store search results with a 1-minute TTL, aligning with the requirement that new posts appear within 1 minute. If cached, return results; otherwise, query the index and cache the result.  
Local Cache: Each search service node maintains an in-memory cache. For 100 simultaneous "Taylor Swift" searches, only one request hits the index, bounding requests to the number of search service nodes (N).  
CDN Caching: Use a CDN with 1-minute cacheable HTTP headers. Edge nodes cache results locally (e.g., in a city), serving subsequent requests without hitting the search service.Trade-Off: Caching reduces index load but risks stale results within the 1-minute window. CDNs are optimal for global distribution but add complexity.

2. High Write Throughput
Challenge: Writes (10x more than reads, e.g., 100K likes/second vs. 10K searches/second) overload the ingestion service, especially during bursts (e.g., New Year’s). Tokenizing posts (e.g., 100 keywords/post) amplifies writes.Solution:  

Kafka Async Processing: Post and like events write to Kafka topics (post-events, like-events), partitioned by post ID. The ingestion service scales horizontally, reading from Kafka with retention for fault tolerance. This buffers spikes, allowing up to 1 minute for processing.  
Batching Likes: Use Flink to batch like events over 30 seconds, summing changes before writing to Kafka. This reduces writes for viral posts (e.g., 1M likes) but is less effective for low-engagement posts.  
Logarithmic Likes: Store log₂(likes) in Redis sorted sets (e.g., 1M likes → 20). Update only when the exponent changes, reducing write frequency. The search service fetches exact like counts for final re-ranking, ensuring precision.Trade-Off: Kafka and batching add latency but ensure scalability. Logarithmic likes sacrifice ranking precision but prioritize viral posts.

3. Redis Write Capacity
Challenge: Tokenization increases writes (e.g., 100 keywords/post × 10K posts/second). A single Redis node (~100K TPS) may not handle this.Solution:  

Redis Cluster: Shard keys across multiple nodes. Initially, use {keyword} as the partition key (e.g., all "Trump" posts on one node).  
Hot Key Mitigation: For hot keywords (e.g., "Taylor Swift"), shard by post ID modulo N (e.g., likes:{keyword}:{postId % 100}). This spreads writes across N nodes but requires the search service to query N shards and merge results.Trade-Off: Keyword sharding simplifies reads but risks hot nodes. Post ID sharding balances writes but increases read complexity. Adjust N dynamically for hot keys.

4. Storage Management
Challenge: Storing all post IDs per keyword (e.g., 10M for "Taylor") consumes significant memory.Solution:  

Capped Indexes: Limit sorted sets to 1,000 post IDs per keyword, reducing size (e.g., N shards × keywords × 1K IDs × 10 bytes).  
Hot/Cold Storage: Store frequent keywords in Redis (hot) and evict rare ones to S3 (cold). Use a Count-Min Sketch to approximate keyword access frequency, evicting those with low counts (e.g., "Stefan" at 12 vs. "Taylor" at 5,000).Trade-Off: Capping and cold storage save memory but increase latency for rare queries. Count-Min Sketch uses minimal space but may overestimate counts.

5. Multi-Word Queries (e.g., "Taylor Swift")
Challenge: Supporting bigrams requires matching consecutive words.Solution:  

Intersection Approach: Split "Taylor Swift" into "Taylor" and "Swift", intersect post IDs, fetch post content from the Post DB, and verify bigram presence.  
Bigram Indexing: Store frequent bigrams (e.g., "Taylor Swift") in Redis sorted sets, identified by Count-Min Sketch. A 100-word post has 99 bigrams, potentially doubling index size.Trade-Off: Intersection is slower but saves space. Bigram indexing speeds up common queries but increases storage. Use Count-Min Sketch to limit bigrams to popular searches.

Conclusion
This design leverages inverted indexes, caching, Kafka, and Redis to meet functional requirements while addressing latency, throughput, and storage challenges. Techniques like batching, logarithmic likes, and hot/cold storage optimize write-heavy workloads, while CDN and local caching ensure fast reads. Count-Min Sketch enhances efficiency for storage and bigram indexing. The system is a starting point, with further optimizations possible for specific constraints.
---------------------------------------------------------------------------
Facebook Post Search System Design
Optimizing Search with Inverted Indexes
To achieve fast searches, we structure data to minimize read latency, using an inverted index approach. Ideally, post IDs for a keyword are pre-sorted by creation time, enabling the search service to retrieve the top 100 posts directly. Since we support sorting by both creation time and like count, a single index can’t cover both. Instead, we create dual indexes per keyword: one for time and one for likes. We use Redis sorted sets, where post IDs are stored with scores based on timestamps or like counts, allowing O(log n) retrieval. The search service queries the appropriate index (e.g., time:{keyword} or likes:{keyword}) and fetches the top N posts. To manage storage, we limit each sorted set to the top 100 post IDs, prioritizing recent or high-engagement posts.
Processing Like Events
The like service notifies the ingestion service of like events to keep indexes updated. Instead of writing directly to the search index, likes are stored in a Likes DB, with a Redis cache tracking like counts (e.g., post:{id}:likes). Like/unlike events update the cache and DB, and changes are published to a Kafka topic (like-events) via CDC for reliability. The ingestion service consumes these events, tokenizes the post’s content, and updates the corresponding Redis sorted sets. Frequent like events, especially for viral posts, create a write bottleneck, but the system meets basic functionality.
Functional Requirements
This setup fulfills the requirements: keyword-based search with sorting by time or likes. The system is functional but requires optimization for non-functional requirements like latency and throughput.
Deep Dives
1. Reducing Read Latency and Handling High Throughput
Challenge: Popular searches (e.g., “Taylor Swift” during a viral event) overload the search service and Redis indexes.Solution:  

Redis Cache: Cache search results in Redis with a 1-minute TTL, ensuring new posts appear within the required timeframe. Cache hits return results immediately; misses trigger an index query and cache update.  
In-Memory Cache: Each search service node maintains a local cache. For 100 concurrent “Taylor Swift” searches, only one request reaches the index, capping requests at the number of nodes (N).  
CDN Integration: Use a CDN to cache results globally with 1-minute cacheable HTTP headers. Edge nodes serve cached results, reducing load on the search service.Trade-Off: Caching minimizes index queries but may serve slightly stale data within 1 minute. CDNs enhance global performance but add setup complexity.

2. Managing High Write Throughput
Challenge: Writes dominate (e.g., 100K likes/second vs. 10K searches/second), and tokenization amplifies write volume (e.g., 100 keywords/post). Bursts (e.g., New Year’s posts) strain the ingestion service.Solution:  

Kafka Queuing: Post and like events write to Kafka topics (post-events, like-events), partitioned by post ID. The ingestion service scales horizontally, consuming events with retention for fault tolerance, handling spikes within 1 minute.  
Like Batching: Use Flink to aggregate like events over 30 seconds, reducing writes for high-engagement posts before publishing to Kafka.  
Log-Based Likes: Store log₂(likes) in Redis sorted sets (e.g., 1M likes → 20), updating only when the exponent changes. The search service re-ranks results using exact like counts from the cache.Trade-Off: Kafka and batching introduce slight delays but ensure scalability. Log-based likes reduce writes but require re-ranking for precision.

3. Scaling Redis Write Capacity
Challenge: Tokenization multiplies writes (e.g., 100 keywords/post × 10K posts/second), potentially exceeding a single Redis node’s ~100K TPS.Solution:  

Redis Cluster Sharding: Distribute keys across nodes, initially using {keyword} as the partition key (e.g., “Trump” posts on one node).  
Handling Hot Keys: For hot keywords (e.g., “Taylor Swift”), shard by post ID modulo N (e.g., likes:{keyword}:{postId % 100}), spreading writes across N nodes. The search service queries N shards and merges results.Trade-Off: Keyword sharding simplifies reads but risks hot nodes. Post ID sharding balances writes but complicates reads. N can be tuned for balance.

4. Controlling Storage Growth
Challenge: Storing millions of post IDs per keyword (e.g., 10M for “Taylor”) consumes excessive memory.Solution:  

Index Limits: Cap sorted sets at 1,000 post IDs per keyword, keeping the index size manageable (e.g., N shards × keywords × 1K IDs × 10 bytes).  
Hot/Cold Partitioning: Keep active keywords in Redis (hot) and move inactive ones to S3 (cold). Use a Count-Min Sketch to estimate keyword frequency, evicting low-count keywords (e.g., “Stefan” at 12 vs. “Taylor” at 5,000).Trade-Off: Capped indexes and cold storage reduce memory but slow down rare queries. Count-Min Sketch is space-efficient but may overestimate frequencies.

5. Supporting Multi-Word Queries (e.g., “Taylor Swift”)
Challenge: Bigrams require matching consecutive words efficiently.Solution:  

Intersection Method: Split “Taylor Swift” into “Taylor” and “Swift”, intersect post IDs, fetch content from the Post DB, and check for the bigram.  
Selective Bigram Indexing: Index frequent bigrams (e.g., “Taylor Swift”) in Redis, using Count-Min Sketch to identify popular pairs. A 100-word post generates 99 bigrams, increasing index size.Trade-Off: Intersection saves space but is slower. Bigram indexing speeds up frequent queries but doubles storage. Count-Min Sketch limits indexing to high-value bigrams.

Conclusion
This design uses Redis sorted sets, Kafka, and caching to deliver keyword searches with time or like-based sorting. Optimizations like CDN caching, Kafka async processing, and logarithmic likes address high read/write throughput. Count-Min Sketch and hot/cold storage manage space efficiently. The system is functional and scalable, with room for further tuning based on specific requirements.
-----------------------------------------------------------------------
Facebook Post Search System Design
Efficient Search with Inverted Indexes
To enable rapid searches, we organize data for low-latency reads using an inverted index. Ideally, post IDs for each keyword are pre-sorted by creation time, allowing the search service to fetch the top 100 posts without sorting. Since we support sorting by creation time and like count, a single index isn’t sufficient. We create two indexes per keyword: one for time and one for likes, stored as Redis sorted sets. Post IDs are scored by timestamp or like count, supporting O(log n) queries. The search service queries the relevant index (e.g., time:{keyword} or likes:{keyword}) and retrieves the top N posts. To control storage, we cap sorted sets at 100 post IDs, focusing on recent or highly engaged posts.
Managing Like Events
The like service updates the ingestion service when like events occur. Likes are persisted in a Likes DB, with a Redis cache tracking counts (e.g., post:{id}:likes). Like/unlike events update the cache and DB, and changes are sent to a Kafka topic (like-events) via CDC for durability. The ingestion service processes these events, tokenizes post content, and updates Redis sorted sets. High-frequency like events, particularly for viral posts, create a write-intensive workload, posing a potential bottleneck.
Functional Requirements
The system supports keyword searches sorted by time or likes, meeting core functionality. Optimizations are needed to address non-functional requirements like latency and throughput.
Deep Dives
1. Minimizing Read Latency and Supporting High Throughput
Challenge: High search volume for trending keywords (e.g., “Taylor Swift” during a news cycle) stresses the search service and Redis indexes.Solution:  

Redis Cache: Store search results in Redis with a 1-minute TTL, ensuring new posts appear within the specified timeframe. Cache hits return results instantly; misses query the index and update the cache.  
Local Cache: Each search service node uses an in-memory cache. For 100 simultaneous “Taylor Swift” searches, only one request hits the index, limiting requests to the number of nodes (N).  
CDN Caching: Deploy a CDN to cache results globally with 1-minute HTTP cache headers. Edge nodes serve cached responses, reducing origin load.Trade-Off: Caching lowers index load but may return slightly stale data within 1 minute. CDNs optimize global access but increase complexity.

2. Handling High Write Throughput
Challenge: Writes outpace reads (e.g., 100K likes/second vs. 10K searches/second), amplified by tokenization (e.g., 100 keywords/post). Spikes (e.g., global events) strain the ingestion service.Solution:  

Kafka Buffering: Write post and like events to Kafka topics (post-events, like-events), partitioned by post ID. The ingestion service scales out, consuming events with retention for fault tolerance, processing within 1 minute.  
Batching Likes: Use Flink to aggregate like events over 30 seconds, consolidating updates for viral posts before writing to Kafka.  
Logarithmic Like Counts: Store log₂(likes) in Redis sorted sets (e.g., 1M likes → 20), updating only when the exponent changes. The search service re-ranks using precise like counts from the cache.Trade-Off: Kafka and batching add latency but ensure scalability. Logarithmic counts reduce writes but require re-ranking for accuracy.

3. Scaling Redis Write Throughput
Challenge: Tokenization multiplies writes (e.g., 100 keywords/post × 10K posts/second), potentially exceeding a single Redis node’s ~100K TPS.Solution:  

Redis Cluster: Shard keys across nodes, initially using {keyword} (e.g., “Trump” posts on one node).  
Mitigating Hot Keys: For high-traffic keywords (e.g., “Taylor Swift”), shard by post ID modulo N (e.g., likes:{keyword}:{postId % 100}), distributing writes across N nodes. The search service queries N shards and merges results.Trade-Off: Keyword sharding simplifies reads but risks hot nodes. Post ID sharding balances writes but increases read overhead. N can be adjusted dynamically.

4. Optimizing Storage
Challenge: Storing millions of post IDs per keyword (e.g., 10M for “Taylor”) demands significant memory.Solution:  

Capped Indexes: Restrict sorted sets to 1,000 post IDs per keyword, keeping indexes compact (e.g., N shards × keywords × 1K IDs × 10 bytes).  
Hot/Cold Storage: Maintain active keywords in Redis (hot) and evict infrequent ones to S3 (cold). A Count-Min Sketch estimates keyword access frequency, removing low-count keywords (e.g., “Stefan” at 12 vs. “Taylor” at 5,000).Trade-Off: Capping and cold storage save memory but slow rare queries. Count-Min Sketch is memory-efficient but may overestimate counts.

5. Multi-Word Queries (e.g., “Taylor Swift”)
Challenge: Bigrams require matching consecutive words efficiently.Solution:  

Intersection-Based Search: Split “Taylor Swift” into “Taylor” and “Swift”, intersect post IDs, fetch content from the Post DB, and verify the bigram.  
Bigram Indexing: Index high-frequency bigrams (e.g., “Taylor Swift”) in Redis, selected via Count-Min Sketch. A 100-word post yields 99 bigrams, increasing index size.Trade-Off: Intersection is space-efficient but slower. Bigram indexing speeds frequent queries but consumes more storage. Count-Min Sketch ensures only popular bigrams are indexed.

Conclusion
This design leverages Redis sorted sets, Kafka, and multi-layered caching to deliver keyword searches with time or like-based sorting. Optimizations like batching, logarithmic likes, and hot/cold storage handle high write volumes, while CDN and local caches ensure low-latency reads. Count-Min Sketch optimizes storage and bigram indexing. The system is robust and adaptable, with potential for further refinement based on specific needs.

Facebook Post Search System Design
Efficient Search with Inverted Indexes
To enable rapid searches, we organize data for low-latency reads using an inverted index. Ideally, post IDs for each keyword are pre-sorted by creation time, allowing the search service to fetch the top 100 posts without sorting. Since we support sorting by creation time and like count, a single index isn’t sufficient. We create two indexes per keyword: one for time and one for likes, stored as Redis sorted sets. Post IDs are scored by timestamp or like count, supporting O(log n) queries. The search service queries the relevant index (e.g., time:{keyword} or likes:{keyword}) and retrieves the top N posts. To control storage, we cap sorted sets at 100 post IDs, focusing on recent or highly engaged posts.
Managing Like Events
The like service updates the ingestion service when like events occur. Likes are persisted in a Likes DB, with a Redis cache tracking counts (e.g., post:{id}:likes). Like/unlike events update the cache and DB, and changes are sent to a Kafka topic (like-events) via CDC for durability. The ingestion service processes these events, tokenizes post content, and updates Redis sorted sets. High-frequency like events, particularly for viral posts, create a write-intensive workload, posing a potential bottleneck.
Functional Requirements
The system supports keyword searches sorted by time or likes, meeting core functionality. Optimizations are needed to address non-functional requirements like latency and throughput.
Deep Dives
1. Minimizing Read Latency and Supporting High Throughput
Challenge: High search volume for trending keywords (e.g., “Taylor Swift” during a news cycle) stresses the search service and Redis indexes.Solution:  

Redis Cache: Store search results in Redis with a 1-minute TTL, ensuring new posts appear within the specified timeframe. Cache hits return results instantly; misses query the index and update the cache.  
Local Cache: Each search service node uses an in-memory cache. For 100 simultaneous “Taylor Swift” searches, only one request hits the index, limiting requests to the number of nodes (N).  
CDN Caching: Deploy a CDN to cache results globally with 1-minute HTTP cache headers. Edge nodes serve cached responses, reducing origin load.Trade-Off: Caching lowers index load but may return slightly stale data within 1 minute. CDNs optimize global access but increase complexity.

2. Handling High Write Throughput
Challenge: Writes outpace reads (e.g., 100K likes/second vs. 10K searches/second), amplified by tokenization (e.g., 100 keywords/post). Spikes (e.g., global events) strain the ingestion service.Solution:  

Kafka Buffering: Write post and like events to Kafka topics (post-events, like-events), partitioned by post ID. The ingestion service scales out, consuming events with retention for fault tolerance, processing within 1 minute.  
Batching Likes: Use Flink to aggregate like events over 30 seconds, consolidating updates for viral posts before writing to Kafka.  
Logarithmic Like Counts: Store log₂(likes) in Redis sorted sets (e.g., 1M likes → 20), updating only when the exponent changes. The search service re-ranks using precise like counts from the cache.Trade-Off: Kafka and batching add latency but ensure scalability. Logarithmic counts reduce writes but require re-ranking for accuracy.

3. Scaling Redis Write Throughput
Challenge: Tokenization multiplies writes (e.g., 100 keywords/post × 10K posts/second), potentially exceeding a single Redis node’s ~100K TPS.Solution:  

Redis Cluster: Shard keys across nodes, initially using {keyword} (e.g., “Trump” posts on one node).  
Mitigating Hot Keys: For high-traffic keywords (e.g., “Taylor Swift”), shard by post ID modulo N (e.g., likes:{keyword}:{postId % 100}), distributing writes across N nodes. The search service queries N shards and merges results.Trade-Off: Keyword sharding simplifies reads but risks hot nodes. Post ID sharding balances writes but increases read overhead. N can be adjusted dynamically.

4. Optimizing Storage
Challenge: Storing millions of post IDs per keyword (e.g., 10M for “Taylor”) demands significant memory.Solution:  

Capped Indexes: Restrict sorted sets to 1,000 post IDs per keyword, keeping indexes compact (e.g., N shards × keywords × 1K IDs × 10 bytes).  
Hot/Cold Storage: Maintain active keywords in Redis (hot) and evict infrequent ones to S3 (cold). A Count-Min Sketch estimates keyword access frequency, removing low-count keywords (e.g., “Stefan” at 12 vs. “Taylor” at 5,000).Trade-Off: Capping and cold storage save memory but slow rare queries. Count-Min Sketch is memory-efficient but may overestimate counts.

5. Multi-Word Queries (e.g., “Taylor Swift”)
Challenge: Bigrams require matching consecutive words efficiently.Solution:  

Intersection-Based Search: Split “Taylor Swift” into “Taylor” and “Swift”, intersect post IDs, fetch content from the Post DB, and verify the bigram.  
Bigram Indexing: Index high-frequency bigrams (e.g., “Taylor Swift”) in Redis, selected via Count-Min Sketch. A 100-word post yields 99 bigrams, increasing index size.Trade-Off: Intersection is space-efficient but slower. Bigram indexing speeds frequent queries but consumes more storage. Count-Min Sketch ensures only popular bigrams are indexed.

Conclusion
This design leverages Redis sorted sets, Kafka, and multi-layered caching to deliver keyword searches with time or like-based sorting. Optimizations like batching, logarithmic likes, and hot/cold storage handle high write volumes, while CDN and local caches ensure low-latency reads. Count-Min Sketch optimizes storage and bigram indexing. The system is robust and adaptable, with potential for further refinement based on specific needs.

-----------------------------------------------------------------------------
Understood. Below is the **formatted version** of the text you uploaded (`Pasted_Text_1750424628833.txt`). I have cleaned up the structure, added appropriate headings and bullet points where necessary, and improved readability — all while keeping your original content intact and avoiding over-modification.

---

# Deep Dives

In a system design interview, especially one focused on infrastructure, it's important to take a holistic view of the system and identify critical bottlenecks. These are often aligned with non-functional requirements like latency, throughput, fault tolerance, and scalability. Let’s walk through how our system holds up against these.

## 1. Low Latency & High Throughput (Read Optimization)

### Problem:
We expect high read volume from users searching for posts using keywords. Many users may be searching for the same popular topics (e.g., “Taylor Swift”) at the same time.

### Solution: Use Caching
- **Local Cache in Search Service**: Each search service maintains its own cache to avoid duplicate calls to the search index.
    - This limits the number of requests hitting the backend to at most `N`, where `N` is the number of search services.
- **CDN for Global Caching**:
    - A Content Delivery Network can serve cached results closer to the user.
    - Set HTTP headers with a short TTL (e.g., 1 minute) to align with our consistency requirement that new posts appear within 1 minute.
    - Popular searches like trending topics will benefit greatly from this global caching layer.

> 💡 **Key Insight:** Always consider caching layers — local, distributed, or CDN-based — when handling high read volumes with repeated queries.

---

## 2. Write Throughput Optimization

### Problem:
Our system has significantly more writes than reads, especially due to likes (10x more than posts). We must ensure ingestion scales well under bursty traffic (e.g., during viral events).

### Solutions:

#### A. Asynchronous Processing with Kafka
- Instead of writing directly to the search index, we publish write events to **Kafka**.
- Ingestion service consumes from Kafka, allowing us to scale horizontally and decouple ingestion from indexing.
- Benefits:
    - Fault-tolerant: If ingestion fails, we can replay messages.
    - Scalable: Add more consumers as needed.

#### B. Batching Like Events
- Likes don’t always change ranking; many happen on already popular posts.
- Batch events every 30 seconds before publishing to Kafka.
- Tools: Flink or custom Kafka batching logic.

#### C. Logarithmic Counting
- Store log values of likes instead of raw numbers.
    - Example: Store `log2(likes)` → if a post reaches 2^16 likes, store 16.
- Only update the index when the exponent changes.
- This dramatically reduces the number of updates to the search index.

> 🧠 **Trade-off**: Approximate sorting vs. reduced write load. Final re-ranking happens in the search service with real-time data.

#### D. Reddis Clustering for Index Writes
- Reddis offers fast in-memory writes but has limits (~100k TPS per node).
- Partition keys by keyword for even distribution across nodes.
- For hot keys (like "Trump" or "Taylor"), use **sharding**:
    - Add shard identifier to key names (e.g., `keyword:time:1`, `keyword:time:2`).
    - Spread writes across multiple nodes.
    - Trade-off: Increased read complexity, since merging results from multiple shards is required.

> 🔑 **Interview Tip**: Be ready to explain your sharding strategy. Consider both read and write patterns.

---

## 3. Storage Optimization

### Problem:
Storing billions of posts and their associated metadata in memory is expensive.

### Solutions:

#### A. Cap Post IDs per Keyword
- Limit the number of post IDs stored per keyword (e.g., top 1,000).
- Ensures bounded growth of the index.

#### B. Hot/Cold Data Separation
- **Hot Data**: Frequently accessed keywords remain in memory (Reddis).
- **Cold Data**: Less frequently accessed keywords are moved to cheaper storage like S3.
- When a query hits cold storage, retrieve the data lazily and return slower results.

#### C. Use Count-Min Sketch for Eviction Decisions
- Count-Min Sketch is a probabilistic data structure used to estimate the frequency of items.
- Helps identify low-frequency keywords that can be evicted from hot storage.
- Small memory footprint makes it ideal for large-scale systems.

> 🛠️ **Use Case**: Track how often each keyword appears in search queries or post content to determine what goes into hot storage.

---

## 4. Multi-Keyword Queries (Bigrams)

### Problem:
How do we handle queries like “Taylor Swift” — two words next to each other?

### Naive Approach:
- Split into “Taylor” and “Swift”, get matching post IDs for each.
- Retrieve full posts from DB and scan manually for adjacency.
- Works, but inefficient.

### Optimized Approach:
- **Index Bigrams**:
    - Break posts into word pairs (bigrams): “Taylor Swift”, “Swift was”, etc.
    - Insert bigrams into the search index just like single words.
- **Trade-off**: Increases index size significantly (~2x), but improves performance.

#### Optimization: Threshold-Based Bigram Indexing
- Use Count-Min Sketch to track popularity of bigrams in search queries.
- Only insert bigrams into the index if they exceed a popularity threshold.
- Avoids bloating the index with rarely searched bigrams.

> 🧩 **Middle Ground Strategy**: Balance between performance and space efficiency using statistical tracking.

---

# Conclusion

This question — designing Facebook Post Search — is commonly asked at all levels, from mid-level to staff engineers.

### Mid-Level Engineers:
- Should understand basic concepts like inverted indexes.
- Demonstrate ability to build a working system, even if not optimal.

### Senior Engineers:
- Identify bottlenecks.
- Propose solutions like Kafka, caching, and logarithmic counting.

### Staff-Level Engineers:
- Show deep knowledge of systems like ElasticSearch.
- Understand trade-offs in indexing strategies, caching, and probabilistic data structures.

We covered several key system design techniques:
- **Caching** at multiple layers (local, distributed, CDN)
- **Inverted Indexes** for fast retrieval
- **Partitioning/Sharding Strategies**
- **Probabilistic Structures** like Count-Min Sketch
- **Handling Multi-Keyword Queries**

These concepts are broadly applicable and should help you tackle similar infra-heavy system design problems.

If you found this helpful, feel free to ask questions in the comments. You can also check out a detailed write-up on our website or book a mock interview with expert coaches on Hello Interview.

Thank you for watching — until next time!

---

📥 **Download Option**:  
You can copy the above content into a file and save it as:
- `Facebook_Post_Search_Design_DeepDives.md` (Markdown)
- `Facebook_Post_Search_Design_DeepDives.txt` (Plain Text)

Let me know if you'd like this in PDF or Word format!
