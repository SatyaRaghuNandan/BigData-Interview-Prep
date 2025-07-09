


Great question! Let's break down the **difference between Leetcode 121** and **Leetcode 122** – both are about buying and selling stocks, but they follow **different trading rules**:

---

## 🧠 **Leetcode 121: Best Time to Buy and Sell Stock**

> 📌 **You are allowed to make only *one* transaction.**
> That means: **Buy once, Sell once.**

### ✅ Goal:

> Maximize profit by choosing **one best day to buy** and **one best day to sell after it.**

---

### ✨ Example:

```
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Buy at 1, Sell at 6 → Profit = 5
```

---

### 🔍 Logic:

* Track the **minimum price so far**
* At each day, compute `price - min_price` and update max profit

---

### ✅ Time: O(n), Space: O(1)

---

---

## 🧠 **Leetcode 122: Best Time to Buy and Sell Stock II**

> 📌 **You can make as many transactions as you want.**
> But: **You must sell before you buy again.**

### ✅ Goal:

> Maximize profit by making **multiple buys and sells** — i.e., profit from **every price increase**.

---

### ✨ Example:

```
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 7
Explanation:
Buy at 1, Sell at 5 → Profit = 4
Buy at 3, Sell at 6 → Profit = 3
Total Profit = 4 + 3 = 7
```

---

### 🔍 Logic:

* Whenever `prices[i] > prices[i-1]`, buy at `i-1` and sell at `i`
* Add all positive differences

---

### ✅ Time: O(n), Space: O(1)

---

## 🔁 Summary Comparison

| Feature                      | LC 121 (Buy & Sell I)       | LC 122 (Buy & Sell II)    |
| ---------------------------- | --------------------------- | ------------------------- |
| Transactions allowed         | 1                           | Unlimited                 |
| Buy before Sell required     | ✅ Yes                       | ✅ Yes                     |
| Strategy                     | Find **best single window** | Accumulate **every gain** |
| Greedy possible?             | ❌ No, needs tracking        | ✅ Yes, local peak/valley  |
| Output (for `[7,1,5,3,6,4]`) | 5                           | 7                         |

---

Let me know if you'd like:

* Java implementations for both
* A side-by-side dry run
* Or to explore dynamic programming variants (LC 123, 188, 309, etc.)



Excellent! Let’s now compare **Leetcode 123: Best Time to Buy and Sell Stock III** with **Leetcode 121 and 122** so you clearly understand the difference in constraints and strategies.

---

## ✅ **Problem Comparison Table**

| Problem | Max Transactions       | Greedy Allowed? | Core Strategy                                |
| ------- | ---------------------- | --------------- | -------------------------------------------- |
| **121** | 1 transaction          | ✅ Yes           | Track min-price and max-profit               |
| **122** | Unlimited              | ✅ Yes           | Add every local profit (greedy)              |
| **123** | Max **2 transactions** | ❌ No            | Use **Dynamic Programming** to track profits |

---

## 🧠 **Leetcode 123: Best Time to Buy and Sell Stock III**

### 📌 You are allowed to **buy and sell at most *two times***

* But you must **sell before you buy again**.
* Transactions must be in order: Buy → Sell → Buy → Sell

---

### ✨ Example:

```text
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation:
Buy at 0, sell at 3 → Profit = 3
Buy at 1, sell at 4 → Profit = 3
Total = 6
```

---

## 🔍 Key Insight:

You want to **maximize the sum of profits from 2 non-overlapping transactions.**

### ❌ Can't use greedy:

* Because you might need to **skip a small profit now** to make a **bigger profit later**.

---

## ✅ DP Solution Idea:

Track 4 states:

| Variable | Meaning                                       |
| -------- | --------------------------------------------- |
| `buy1`   | Max profit after 1st **buy** (initially `-∞`) |
| `sell1`  | Max profit after 1st **sell**                 |
| `buy2`   | Max profit after 2nd **buy** (after 1st sell) |
| `sell2`  | Max profit after 2nd **sell**                 |

### Transition:

```java
buy1  = max(buy1, -price);
sell1 = max(sell1, buy1 + price);
buy2  = max(buy2, sell1 - price);
sell2 = max(sell2, buy2 + price);
```

---

## 🧮 Dry Run:

```
prices = [3,3,5,0,0,3,1,4]

buy1  = -3
sell1 = 0
buy2  = -3
sell2 = 0

→ sell1 peaks at 3, sell2 peaks at 6 → ✅
```

---

## ✅ Time & Space Complexity

| Metric    | Value |
| --------- | ----- |
| **Time**  | O(n)  |
| **Space** | O(1)  |

> We only track 4 variables throughout.

---

## 🔁 Comparison Recap

| Problem | Max Transactions | Strategy        | Greedy? | Time |
| ------- | ---------------- | --------------- | ------- | ---- |
| LC 121  | 1                | Track min price | ✅ Yes   | O(n) |
| LC 122  | Unlimited        | Local gains     | ✅ Yes   | O(n) |
| LC 123  | 2                | DP (4 vars)     | ❌ No    | O(n) |

---

Let me know if you'd like:

* Java implementation with Telugu comments
* Code comparison across LC 121, 122, 123
* Extension to LC 188 (k transactions) or LC 309 (Cooldown)


