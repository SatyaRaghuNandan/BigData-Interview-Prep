Perfect! Below is the **Java version** of your modular `addStrings` logic (including **decimal support**) from the Python version.

---

## ✅ Java Implementation (Modular + Decimal Support)

```java
public class ModularStringAddition {

    // 🔹 Helper: Normalize lengths by padding with '0'
    private String[] normalizeLengths(String s1, String s2, boolean padRight) {
        int maxLength = Math.max(s1.length(), s2.length());
        if (padRight) {
            s1 = String.format("%-" + maxLength + "s", s1).replace(' ', '0');
            s2 = String.format("%-" + maxLength + "s", s2).replace(' ', '0');
        } else {
            s1 = String.format("%" + maxLength + "s", s1).replace(' ', '0');
            s2 = String.format("%" + maxLength + "s", s2).replace(' ', '0');
        }
        return new String[]{s1, s2};
    }

    // 🔹 Helper: Add two whole number strings
    private String[] addIntegerStrings(String num1, String num2, int carry) {
        String[] normalized = normalizeLengths(num1, num2, false);
        num1 = normalized[0];
        num2 = normalized[1];

        StringBuilder result = new StringBuilder();
        for (int i = num1.length() - 1; i >= 0; i--) {
            int sum = (num1.charAt(i) - '0') + (num2.charAt(i) - '0') + carry;
            result.append(sum % 10);
            carry = sum / 10;
        }

        return new String[]{result.reverse().toString(), String.valueOf(carry)};
    }

    // 🔹 Helper: Add two decimal strings (fractional part)
    private String[] addDecimalStrings(String dec1, String dec2) {
        String[] normalized = normalizeLengths(dec1, dec2, true);
        dec1 = normalized[0];
        dec2 = normalized[1];

        StringBuilder result = new StringBuilder();
        int carry = 0;
        for (int i = dec1.length() - 1; i >= 0; i--) {
            int sum = (dec1.charAt(i) - '0') + (dec2.charAt(i) - '0') + carry;
            result.append(sum % 10);
            carry = sum / 10;
        }

        return new String[]{result.reverse().toString(), String.valueOf(carry)};
    }

    // 🔹 Basic case: Add two whole numbers
    public String addStrings(String num1, String num2) {
        String[] sumAndCarry = addIntegerStrings(num1, num2, 0);
        String result = sumAndCarry[0];
        int carry = Integer.parseInt(sumAndCarry[1]);

        return (carry > 0 ? carry : "") + result;
    }

    // 🔹 Extended case: Add decimals
    public String addStringsWithDecimal(String num1, String num2) {
        String[] parts1 = num1.split("\\.");
        String[] parts2 = num2.split("\\.");

        String int1 = parts1[0];
        String dec1 = parts1.length > 1 ? parts1[1] : "";

        String int2 = parts2[0];
        String dec2 = parts2.length > 1 ? parts2[1] : "";

        // Step 1: Add fractional parts
        String[] decimalResult = addDecimalStrings(dec1, dec2);
        String decSum = decimalResult[0];
        int carry = Integer.parseInt(decimalResult[1]);

        // Step 2: Add whole parts with carry from decimal addition
        String[] intResult = addIntegerStrings(int1, int2, carry);
        String intSum = intResult[0];
        int finalCarry = Integer.parseInt(intResult[1]);

        if (finalCarry > 0) {
            intSum = finalCarry + intSum;
        }

        // Step 3: Trim trailing zeros from decimal part
        decSum = decSum.replaceFirst("0+$", "");

        return decSum.isEmpty() ? intSum : intSum + "." + decSum;
    }

    // ✅ Demo
    public static void main(String[] args) {
        ModularStringAddition msa = new ModularStringAddition();

        System.out.println(msa.addStrings("123", "789"));               // "912"
        System.out.println(msa.addStringsWithDecimal("123.45", "78.9")); // "202.35"
        System.out.println(msa.addStringsWithDecimal("1.999", "2.001")); // "4"
        System.out.println(msa.addStringsWithDecimal("0.1", "0.02"));    // "0.12"
        System.out.println(msa.addStringsWithDecimal("10", "5.25"));     // "15.25"
        System.out.println(msa.addStringsWithDecimal("100.000", "0.999"));// "100.999"
    }
}
```

---

## ✅ Notes for Interview Prep

### Breakdown by Responsibility:

| Function                | Purpose                          |
| ----------------------- | -------------------------------- |
| `normalizeLengths`      | Pads strings left/right with '0' |
| `addIntegerStrings`     | Adds two integer strings (L→R)   |
| `addDecimalStrings`     | Adds decimal strings (R→L)       |
| `addStrings`            | Pure integer addition            |
| `addStringsWithDecimal` | Handles decimal + integer logic  |

---

Would you like the **JUnit tests for this Java version** next?
