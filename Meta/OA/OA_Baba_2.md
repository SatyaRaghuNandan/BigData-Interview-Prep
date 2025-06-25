Awesome! Let's simulate a **realistic Meta-style CodeSignal OCA mock interview** — complete with:

- A **progressive 4-level problem**
- Increasing complexity
- **Edge cases**
- **Test cases (with expected outputs)**
- **Time constraints (2 hours)**

---

## 🧪 Mock Interview: Banking System Implementation

### 📌 Problem Title:  
**Implement a Customer-Centric Banking Platform**

You are tasked with implementing a system that allows users to:
- Create accounts
- Make deposits, withdrawals, and transfers
- Record purchases for cashback
- Identify top customers
- Merge customer profiles

This will be split into **4 levels**, each building on the previous.

---

## ⏱️ Time Limit: 2 Hours  
Try to solve as many levels as you can. Focus on correctness first, then performance.

---

## 🔁 Level 1: Account Management & Transactions  
**Estimated Time: 20–30 minutes**

### ✅ Features:
- `createAccount(ownerId)` – returns accountId
- `getBalance(accountId)`
- `deposit(accountId, amount)`
- `withdraw(accountId, amount)`
- `transfer(fromAccountId, toAccountId, amount)`

### 📝 Notes:
- Accounts start at $0.
- Transfers should deduct from one account and add to another.
- Return `false` for invalid operations (e.g., insufficient balance).

### 🧪 Sample Test Case:
```java
BankingSystem bank = new BankingSystem();
String a1 = bank.createAccount("u1"); // "acc1"
String a2 = bank.createAccount("u2"); // "acc2"

bank.deposit(a1, 100);         // true
bank.transfer(a1, a2, 50);     // true
bank.withdraw(a2, 20);         // true

bank.getBalance(a1);           // 50.0
bank.getBalance(a2);           // 30.0
```

---

## 💸 Level 2: Cashback Tracking with Categories  
**Estimated Time: 30–40 minutes**

### ✅ Features:
- `recordPurchase(accountId, category, amount)`
- `applyCashback(accountId)` – applies 1% base rate or higher based on category

### 📝 Notes:
- Categories like `"grocery"`, `"travel"`, `"dining"` have different cashback rates.
- After applying cashback, reset purchase history.

### 🧪 Sample Test Case:
```java
bank.recordPurchase(a1, "grocery", 200);   // true
bank.recordPurchase(a1, "travel", 100);    // true

bank.applyCashback(a1);  // adds (200 * 0.02 + 100 * 0.015) = $5.5 → total $55.5
bank.getBalance(a1);      // 55.5
```

---

## 🔗 Level 3: Merging Customers  
**Estimated Time: 40–50 minutes**

### ✅ Features:
- `mergeCustomers(ownerId1, ownerId2)` – merge all their accounts into one
- The merged customer keeps all balances, purchase history, etc.

### 📝 Notes:
- Only allow merging if both exist.
- Prevent cycles or duplicate merges.
- After merge, only one primary account remains active per user.

### 🧪 Sample Test Case:
```java
String a3 = bank.createAccount("u1");  // already has a1
bank.deposit(a3, 100);                 // now u1 has two accounts

bank.mergeCustomers("u1", "u2");       // merge u2 into u1
bank.getBalance(a1);                   // 55.5 + 30 (from transfer) + 100 (a3) = 185.5
```

---

## 📈 Level 4: Batch Analysis – Top Customers  
**Estimated Time: Remaining time**

### ✅ Features:
- `getTopNSpenders(n, month)` – returns up to `n` customer IDs by total spending in given month

### 📝 Notes:
- Month is in format `"YYYY-MM"`
- Use transaction timestamps to filter
- Spending includes purchases and transfers

### 🧪 Sample Test Case:
```java
bank.recordPurchase(a1, "grocery", 200);  // timestamped
bank.recordPurchase(a2, "travel", 300);   // also timestamped

List<String> top = bank.getTopNSpenders(2, "2025-04");
// Expected: ["u1", "u2"] or ["u2", "u1"], depending on total spend
```

---

## 🧠 Bonus Challenge (Optional)
If time permits, implement:
- Interest calculation on monthly average balance
- Fraud detection rules (e.g., large transfers at odd hours)
- Export transaction history in JSON format

---

## ✅ Final Submission Checklist

| Feature | Implemented? |
|--------|--------------|
| Level 1: CRUD operations | ☐ |
| Level 2: Metadata (categories, timestamps) | ☐ |
| Level 3: Merging customers | ☐ |
| Level 4: Batch analysis (top customers by month) | ☐ |
| Edge Cases (invalid transfers, negative values, same account) | ☐ |

---

## 📦 Java Template to Start With

Here’s a basic class structure you can use to code this out:

```java
import java.util.*;

public class BankingSystem {
    private int accountCounter = 0;
    private Map<String, Double> balances = new HashMap<>();
    private Map<String, List<String>> ownerToAccounts = new HashMap<>();
    private Map<String, Map<String, Double>> categorySpending = new HashMap<>();
    private Map<String, List<Transaction>> transactionHistory = new HashMap<>();

    static class Transaction {
        String accountId;
        String type; // deposit, withdrawal, transfer_out, transfer_in
        double amount;
        long timestamp;

        Transaction(String accountId, String type, double amount, long timestamp) {
            this.accountId = accountId;
            this.type = type;
            this.amount = amount;
            this.timestamp = timestamp;
        }
    }

    // Level 1
    public String createAccount(String ownerId) { /* ... */ }
    public Double getBalance(String accountId) { /* ... */ }
    public boolean deposit(String accountId, double amount) { /* ... */ }
    public boolean withdraw(String accountId, double amount) { /* ... */ }
    public boolean transfer(String fromAccountId, String toAccountId, double amount) { /* ... */ }

    // Level 2
    public boolean recordPurchase(String accountId, String category, double amount) { /* ... */ }
    public boolean applyCashback(String accountId) { /* ... */ }

    // Level 3
    public boolean mergeCustomers(String ownerId1, String ownerId2) { /* ... */ }

    // Level 4
    public List<String> getTopNSpenders(int n, String month) { /* ... */ }
}
```

---

## 🧾 Want Me to Provide a Solution?

I can provide a **complete solution template** with comments, or walk through how to approach each level under time pressure.

Also, I can generate:
- More test cases with edge cases
- Time-tracking tips
- Performance optimization ideas

Just let me know what you'd like next!
