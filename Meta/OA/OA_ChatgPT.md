Excellent question. Here's a detailed breakdown of **how Meta typically asks questions in the CodeSignal Online Assessment (OA)** based on real candidate reports and consistent patterns across multiple interviews:

---

## ✅ How Meta CodeSignal OA Is Structured

### 🧠 Format

* **One real-world inspired system design problem**, broken into **4 levels**
* You must **pass all tests for one level** to unlock the next
* **Duration**: 70–120 minutes
* **Languages**: Python, Java, C++, JavaScript (your choice)
* **Environment**: CodeSignal IDE — basic, limited features

---

## 📦 Problem Presentation Style

The **problem unfolds progressively**. You start with **basic CRUD**, and after solving it successfully, you see the next part of the prompt.

Here's how it feels at each level:

---

## 🧾 Example Flow (Banking System – as asked by Meta)

### ✅ Level 1 – Basic CRUD

> Implement a banking system that supports:
>
> * `create_account(account_id: str, initial_balance: int)`
> * `deposit(account_id: str, amount: int)`
> * `withdraw(account_id: str, amount: int)`
> * `get_balance(account_id: str)`
>
> Constraints:
>
> * No duplicate accounts
> * All balances must remain ≥ 0
> * Invalid operations should silently fail

**➡️ You implement this and pass all test cases. Then Level 2 unlocks.**

---

### ✅ Level 2 – Add Metadata & Logs

> Extend your system to track a **transaction log per account**:
>
> * `get_transaction_log(account_id: str) -> List[str]`
>
> Logs must include:
>
> * Deposits (`\"Deposited 100\"`)
> * Withdrawals
> * Transfers (added in this level)
>
> Add:
>
> * `transfer(from_account: str, to_account: str, amount: int)`
>
> Metadata: Update each account's `lastTransactionDate` on any operation.

**➡️ Now you’re maintaining state and handling formatting.**

---

### ✅ Level 3 – Customer Relationships & Derived Logic

> Introduce customers who can own one or more accounts:
>
> * `create_customer(customer_id: str)`
> * `assign_account(customer_id: str, account_id: str)`
> * `get_customer_balance(customer_id: str)`
>
> Add cashback logic:
>
> * Deposits > 1000 should add 2% cashback
>
> Add analytics:
>
> * `get_top_customers(k: int)` → top-K by total balance

**➡️ Requires refactoring your earlier models to support relationships.**

---

### ✅ Level 4 – Batch Ops, Merges, and System Insights

> Support customer merging and large-scale queries:
>
> * `merge_customers(customer_id_1, customer_id_2)` → merges accounts
> * `get_richest_account()`
> * `get_total_cash_in_bank()`
>
> Constraints:
>
> * Merges must preserve metadata and logs
> * Ties broken lexicographically

**➡️ Focus here is correctness, bulk operations, and metadata usage.**

---

## 🔍 Key Characteristics of Meta OA Style

| Feature                       | Description                                                   |
| ----------------------------- | ------------------------------------------------------------- |
| 📚 Very verbose spec          | The prompt is intentionally **long and full of corner cases** |
| 🔁 Progressive levels         | You can't see Level 2 until you finish Level 1                |
| 🔒 Gated test cases           | All test cases must pass to unlock the next level             |
| 🧱 Requires OOP & refactoring | If you hardcode Level 1, you’ll struggle later                |
| 🚫 No partial credit          | You must handle all edge cases as described                   |
| 📈 Increasing complexity      | Level 3–4 require time management and abstraction             |

---

## 💡 Tips to Succeed

1. **Use Classes (OOP)** from the start — e.g., `Account`, `Customer`, `BankSystem`
2. **Modularize** every feature (`deposit()`, `transfer()`), even in Level 1
3. **Read the spec 2–3 times** — it's long for a reason
4. **Expect edge cases** — zero balances, ties, reassignments, invalid inputs
5. **Don’t over-optimize** — prioritize passing test cases

---

## 🛠 Real Meta OA Problem Themes (past years)

| Domain              | Problem Summary                              |
| ------------------- | -------------------------------------------- |
| 🏦 Banking System   | Accounts, transfers, logs, cashback, merging |
| 🛒 Shopping Cart    | Add/remove items, discounts, bundle pricing  |
| 📁 File System      | Path creation, permissions, hierarchy        |
| 📧 Messaging System | Group chats, unread messages, merging users  |
| 🧾 Order Processing | Batches, status updates, bulk exports        |

---

Would you like me to:

* Simulate a full **4-level Meta OA** in CodeSignal format?
* Provide **practice prompts** for each level with hidden specs like the real test?
* Generate **test case structure** to validate your solution offline?

Let me know how you want to prep further!
