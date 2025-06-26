
package Meta_Banking.baba_Process;

import java.util.*;
import java.util.stream.Collectors;


public class BankingSystem {

    public int accountCounter = 0;
    public Map<String, Double> balances = new HashMap<>();
    public Map<String, List<String>> ownerToAccounts = new HashMap<>();
    public Map<String, Map<String, Double>> categorySpending = new HashMap<>();
    public Map<String, List<Transaction>> transactionHistory = new HashMap<>();





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
        transactionHistory.computeIfAbsent(accountId, k -> new ArrayList<>())
                .add(new Transaction(accountId, "deposit", amount, System.currentTimeMillis()));
        return true;
    }

    public boolean withdraw(String accountId, double amount) {
        if (amount <= 0 || !balances.containsKey(accountId)) return false;
        double current = balances.get(accountId);
        if (current < amount) return false;
        balances.put(accountId, current - amount);
        transactionHistory.computeIfAbsent(accountId, k -> new ArrayList<>())
                .add(new Transaction(accountId, "withdrawal", amount, System.currentTimeMillis()));
        return true;
    }

    public boolean transfer(String fromAccountId, String toAccountId, double amount) {
        if (fromAccountId.equals(toAccountId)) return false;
        if (amount <= 0 || !balances.containsKey(fromAccountId) || !balances.containsKey(toAccountId))
            return false;
        double fromBalance = balances.get(fromAccountId);
        if (fromBalance < amount) return false;

        balances.put(fromAccountId, fromBalance - amount);
        balances.put(toAccountId, balances.get(toAccountId) + amount);

        transactionHistory.computeIfAbsent(fromAccountId, k -> new ArrayList<>())
                .add(new Transaction(fromAccountId, "transfer_out", amount, System.currentTimeMillis()));
        transactionHistory.computeIfAbsent(toAccountId, k -> new ArrayList<>())
                .add(new Transaction(toAccountId, "transfer_in", amount, System.currentTimeMillis()));

        return true;
    }

    // Level 2
    public boolean recordPurchase(String accountId, String category, double amount) {
        if (amount <= 0 || !balances.containsKey(accountId)) return false;
        categorySpending.computeIfAbsent(accountId, k -> new HashMap<>())
                .compute(category, (k, v) -> v == null ? amount : v + amount);
        transactionHistory.computeIfAbsent(accountId, k -> new ArrayList<>())
                .add(new Transaction(accountId, "purchase", amount, System.currentTimeMillis()));
        return true;
    }

    public boolean applyCashback(String accountId) {
        if (!categorySpending.containsKey(accountId)) return false;
        Map<String, Double> spending = categorySpending.remove(accountId);
        double totalCashback = 0.0;

        for (Map.Entry<String, Double> entry : spending.entrySet()) {
            String category = entry.getKey();
            double amount = entry.getValue();

            double rate = switch (category) {
                case "grocery" -> 0.02;
                case "travel" -> 0.015;
                case "dining" -> 0.012;
                default -> 0.01;
            };

            totalCashback += amount * rate;
        }

        if (totalCashback > 0) {
            balances.put(accountId, balances.get(accountId) + totalCashback);
            return true;
        }

        return false;
    }

    // Level 3
    public String mergeCustomers(String ownerId1, String ownerId2) {
        if (!ownerToAccounts.containsKey(ownerId1) || !ownerToAccounts.containsKey(ownerId2))
            return null;

        if (ownerId1.equals(ownerId2)) return ownerId1;

        List<String> accounts1 = ownerToAccounts.get(ownerId1);
        List<String> accounts2 = ownerToAccounts.remove(ownerId2);

        String primaryAccountId = accounts1.get(0);

        for (String accId : accounts2) {
            if (!accId.equals(primaryAccountId)) {
                double balance = balances.get(accId);
                balances.put(primaryAccountId, balances.get(primaryAccountId) + balance);
                balances.remove(accId);
                transactionHistory.merge(primaryAccountId,
                        transactionHistory.getOrDefault(accId, new ArrayList<>()),
                        (oldList, newList) -> {
                            oldList.addAll(newList);
                            return oldList;
                        });
                transactionHistory.remove(accId);
            }
        }

        accounts1.addAll(accounts2);
        ownerToAccounts.put(ownerId1, accounts1);

        return primaryAccountId;
    }

    // Level 4
    private long[] getMonthTimestampRange(String yearMonth) {
        String[] parts = yearMonth.split("-");
        int year = Integer.parseInt(parts[0]);
        int month = Integer.parseInt(parts[1]) - 1;

        Calendar cal = Calendar.getInstance();
        cal.set(year, month, 1, 0, 0, 0);
        long start = cal.getTimeInMillis();

        cal.add(Calendar.MONTH, 1);
        long end = cal.getTimeInMillis();

        return new long[]{start, end};
    }

    public List<String> getTopNSpenders(int n, String month) {
        long[] timeRange = getMonthTimestampRange(month);
        long start = timeRange[0];
        long end = timeRange[1];

        Map<String, Double> ownerSpending = new HashMap<>();

        for (Map.Entry<String, List<Transaction>> entry : transactionHistory.entrySet()) {
            String accountId = entry.getKey();
            String ownerId = null;

            for (Map.Entry<String, List<String>> ownerEntry : ownerToAccounts.entrySet()) {
                if (ownerEntry.getValue().contains(accountId)) {
                    ownerId = ownerEntry.getKey();
                    break;
                }
            }

            if (ownerId == null) continue;

            double totalSpent = 0.0;
            for (Transaction t : entry.getValue()) {
                if (t.timestamp >= start && t.timestamp < end) {
                    if (t.type.equals("purchase") || t.type.equals("transfer_out")) {
                        totalSpent += t.amount;
                    }
                }
            }

            ownerSpending.merge(ownerId, totalSpent, Double::sum);
        }

        return ownerSpending.entrySet().stream()
                .sorted((a, b) -> Double.compare(b.getValue(), a.getValue()))
                .limit(n)
                .map(Map.Entry::getKey)
                .collect(Collectors.toList());
    }

}
