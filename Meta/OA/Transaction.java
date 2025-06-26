package Meta_Banking.baba_Process;

public class Transaction {
    String accountId;
    String type;
    double amount;
    long timestamp;

    Transaction(String accountId, String type, double amount, long timestamp) {
        this.accountId = accountId;
        this.type = type;
        this.amount = amount;
        this.timestamp = timestamp;
    }
}
