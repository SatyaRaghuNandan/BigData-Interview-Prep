package Meta_Banking.baba_Process;

import java.util.ArrayList;
import java.util.Calendar;
import java.util.HashMap;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        BankingSystem bank = new BankingSystem();

        String a1 = bank.createAccount("u1");
        String a2 = bank.createAccount("u2");
        String a3 = bank.createAccount("u3");

        bank.deposit(a1, 100);         // true
        bank.transfer(a1, a2, 50);     // true
        bank.withdraw(a2, 20);         // true

        System.out.println("Balance a1: " + bank.getBalance(a1)); // 50.0
        System.out.println("Balance a2: " + bank.getBalance(a2)); // 30.0

        bank.recordPurchase(a1, "grocery", 200);   // true
        bank.recordPurchase(a1, "travel", 100);    // true
        bank.applyCashback(a1);                    // adds $5.5
        System.out.println("Balance after cashback: " + bank.getBalance(a1)); // 55.5

        bank.mergeCustomers("u1", "u2");           // merges u2 into u1
        System.out.println("Balance a1 after merge: " + bank.getBalance(a1)); // 85.5

        simulateAprilPurchases(bank, a1, a2, a3);

        List<String> topSpenders = bank.getTopNSpenders(2, "2025-04");
        System.out.println("Top 2 spenders in April 2025: " + topSpenders);
    }

    private static void simulateAprilPurchases(BankingSystem bank, String a1, String a2, String a3) {
        Calendar cal = Calendar.getInstance();
        cal.set(2025, Calendar.APRIL, 15);
        long fixedTime = cal.getTimeInMillis();

        injectPurchase(bank, a1, "grocery", 200, fixedTime);
        injectPurchase(bank, a1, "travel", 100, fixedTime);

        injectPurchase(bank, a2, "dining", 150, fixedTime);
        injectPurchase(bank, a2, "grocery", 250, fixedTime);

        injectPurchase(bank, a3, "grocery", 300, fixedTime);
    }

    private static void injectPurchase(BankingSystem bank, String accountId, String category, double amount, long timestamp) {
        Transaction transaction = new Transaction(accountId, "purchase", amount, timestamp);
        bank.transactionHistory.computeIfAbsent(accountId, k -> new ArrayList<>()).add(transaction);
        bank.categorySpending.computeIfAbsent(accountId, k -> new HashMap<>())
                .compute(category, (k, v) -> v == null ? amount : v + amount);
    }
}
