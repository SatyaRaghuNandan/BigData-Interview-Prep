Haha, fair point — and I appreciate the callout! You're absolutely right: **Meta's CodeSignal assessment is unique**, and while GPT/LLM-generated code can help with structure and logic, it often doesn't fully reflect the **specific style, constraints, or edge cases** you'll face in a real Meta-style OCA.

Let’s go deeper and simulate something that feels **authentic to what you'd see at Meta**, including:

- A **realistic problem statement**
- **Progressive levels**
- **Edge cases**
- **Time pressure realism**
- **No reliance on classes like `Account` unless necessary**

---

## 🧪 Meta CodeSignal OCA - Sample Problem (Level 1–4)

### 💼 **Problem Title**: Implement a Simple Bank Transaction System

You are tasked with implementing a system that allows users to create accounts, make deposits, withdrawals, transfers, and eventually identify top customers and merge accounts.

This will be split into **4 levels**, increasing in complexity. Each level builds upon the previous one.

We’ll implement this in Java.

---

## ✅ Level 1: Account Management & Transactions

### Requirements:
- Create account with an owner ID
- Deposit money
- Withdraw money
- Get balance

```java
import java.util.*;

public class BankingSystem {
    private Map<String, Double> balances = new HashMap<>();
    private int accountCounter = 0;

    // Creates a new account for ownerId and returns accountId
    public String createAccount(String ownerId) {
        String accountId = "acc" + (++accountCounter);
        balances.put(accountId, 0.0);
        return accountId;
    }

    // Returns balance of given accountId or null if not found
    public Double getBalance(String accountId) {
        return balances.get(accountId);
    }

    // Deposit amount into accountId
    public boolean deposit(String accountId, double amount) {
        if (amount <= 0 || !balances.containsKey(accountId)) return false;
        balances.put(accountId, balances.get(accountId) + amount);
        return true;
    }

    // Withdraw amount from accountId
    public boolean withdraw(String accountId, double amount) {
        if (amount <= 0 || !balances.containsKey(accountId)) return false;
        double current = balances.get(accountId);
        if (current < amount) return false;
        balances.put(accountId, current - amount);
        return true;
    }
}
```

---

## 💸 Level 2: Add Cashback Tracking

### Requirements:
- Track purchases made using each account
- Apply 1% cashback on total purchase amount

```java
// Add inside the class
private Map<String, Double> purchases = new HashMap<>();

// Record a purchase
public boolean recordPurchase(String accountId, double amount) {
    if (amount <= 0 || !balances.containsKey(accountId)) return false;
    purchases.put(accountId, purchases.getOrDefault(accountId, 0.0) + amount);
    return true;
}

// Apply 1% cashback to the account
public boolean applyCashback(String accountId) {
    if (!purchases.containsKey(accountId)) return false;
    double cashback = purchases.get(accountId) * 0.01;
    balances.put(accountId, balances.get(accountId) + cashback);
    purchases.remove(accountId); // Reset after applying
    return true;
}
```

---

## 🔗 Level 3: Transfer Between Accounts

### Requirements:
- Allow transferring funds between accounts
- Deduct from source, add to destination
- Handle invalid cases

```java
// Add this method
public boolean transfer(String fromAccountId, String toAccountId, double amount) {
    if (fromAccountId.equals(toAccountId)) return false;
    if (amount <= 0) return false;
    if (!balances.containsKey(fromAccountId) || !balances.containsKey(toAccountId))
        return false;

    double fromBalance = balances.get(fromAccountId);
    if (fromBalance < amount) return false;

    balances.put(fromAccountId, fromBalance - amount);
    balances.put(toAccountId, balances.get(toAccountId) + amount);
    return true;
}
```

---

## 🏆 Level 4: Identify Top N Customers by Total Spent

### Requirements:
- Return list of up to N customer IDs who have spent the most across all their accounts

To do this, we need a mapping from **ownerId → List<accountId>**.

### Final Code So Far:

```java
import java.util.*;
import java.util.stream.Collectors;

public class BankingSystem {
    private Map<String, Double> balances = new HashMap<>();
    private Map<String, Double> purchases = new HashMap<>();
    private Map<String, List<String>> ownerToAccounts = new HashMap<>();
    private int accountCounter = 0;

    // Level 1
    public String createAccount(String ownerId) {
        String accountId = "acc" + (++accountCounter);
        balances.put(accountId, 0.0);
        ownerToAccounts.computeIfAbsent(ownerId, k -> new ArrayList<>()).add(accountId);
        return accountId;
    }

    public Double getBalance(String accountId) {
        return balances.get(accountId);
    }

    public boolean deposit(String accountId, double amount) {
        if (amount <= 0 || !balances.containsKey(accountId)) return false;
        balances.put(accountId, balances.get(accountId) + amount);
        return true;
    }

    public boolean withdraw(String accountId, double amount) {
        if (amount <= 0 || !balances.containsKey(accountId)) return false;
        double current = balances.get(accountId);
        if (current < amount) return false;
        balances.put(accountId, current - amount);
        return true;
    }

    // Level 2
    public boolean recordPurchase(String accountId, double amount) {
        if (amount <= 0 || !balances.containsKey(accountId)) return false;
        purchases.put(accountId, purchases.getOrDefault(accountId, 0.0) + amount);
        return true;
    }

    public boolean applyCashback(String accountId) {
        if (!purchases.containsKey(accountId)) return false;
        double cashback = purchases.get(accountId) * 0.01;
        balances.put(accountId, balances.get(accountId) + cashback);
        purchases.remove(accountId);
        return true;
    }

    // Level 3
    public boolean transfer(String fromAccountId, String toAccountId, double amount) {
        if (fromAccountId.equals(toAccountId)) return false;
        if (amount <= 0) return false;
        if (!balances.containsKey(fromAccountId) || !balances.containsKey(toAccountId))
            return false;

        double fromBalance = balances.get(fromAccountId);
        if (fromBalance < amount) return false;

        balances.put(fromAccountId, fromBalance - amount);
        balances.put(toAccountId, balances.get(toAccountId) + amount);
        return true;
    }

    // Level 4
    public List<String> getTopNSpenders(int n) {
        Map<String, Double> ownerSpending = new HashMap<>();

        for (Map.Entry<String, Double> entry : purchases.entrySet()) {
            String accountId = entry.getKey();
            String ownerId = null;

            for (Map.Entry<String, List<String>> ownerEntry : ownerToAccounts.entrySet()) {
                if (ownerEntry.getValue().contains(accountId)) {
                    ownerId = ownerEntry.getKey();
                    break;
                }
            }

            if (ownerId != null) {
                ownerSpending.merge(ownerId, entry.getValue(), Double::sum);
            }
        }

        return ownerSpending.entrySet().stream()
                .sorted((a, b) -> Double.compare(b.getValue(), a.getValue()))
                .limit(n)
                .map(Map.Entry::getKey)
                .collect(Collectors.toList());
    }
}
```

---

## ⚠️ Notes for Real Meta Assessment

- **No helper classes** like `Account` are needed unless specified.
- **Use maps aggressively** to track relationships (`accountId → ownerId`, `accountId → purchases`, etc.)
- **Edge cases matter**: e.g., same account for transfer, zero/negative values, multiple accounts per user.
- **Read specs carefully**, even if they feel arbitrary.
- **Don’t over-engineer early on** — you may need to refactor as levels progress.

---

## ✅ Want More Practice?

Would you like me to give you:
- A **timed mock version** of this problem?
- Another system (e.g., ride-sharing, messaging, or fraud detection)?
- A downloadable runnable Java file?
- Or explain how to debug/test this kind of system during the test?

Just say the word — happy to help you nail this!
