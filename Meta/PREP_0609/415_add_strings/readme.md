class Solution:
    # 🔹 Helper: Normalize lengths by padding with '0'
    def normalize_lengths(self, num1: str, num2: str, pad_right=False) -> tuple[str, str]:
        max_len = max(len(num1), len(num2))
        if pad_right:
            return num1.ljust(max_len, '0'), num2.ljust(max_len, '0')
        else:
            return num1.zfill(max_len), num2.zfill(max_len)

    # 🔹 Helper: Add two numeric strings (right to left)
    def add_integer_strings(self, num1: str, num2: str, carry=0) -> tuple[str, int]:
        num1, num2 = self.normalize_lengths(num1, num2)
        result = []
        for i in range(len(num1) - 1, -1, -1):
            total = int(num1[i]) + int(num2[i]) + carry
            result.append(str(total % 10))
            carry = total // 10
        return ''.join(reversed(result)), carry

    # 🔹 Helper: Add two decimal strings (left to right, carry goes to whole part)
    def add_decimal_strings(self, dec1: str, dec2: str) -> tuple[str, int]:
        dec1, dec2 = self.normalize_lengths(dec1, dec2, pad_right=True)
        result = []
        carry = 0
        for i in range(len(dec1) - 1, -1, -1):
            total = int(dec1[i]) + int(dec2[i]) + carry
            result.append(str(total % 10))
            carry = total // 10
        return ''.join(reversed(result)), carry

    # 🔹 Case 1: Standard addStrings (whole numbers only)
    def addStrings(self, num1: str, num2: str) -> str:
        result, carry = self.add_integer_strings(num1, num2)
        if carry:
            result = str(carry) + result
        return result

    # 🔹 Case 2: Add decimals (e.g., "123.45" + "78.9")
    def addStringsWithDecimal(self, num1: str, num2: str) -> str:
        # Split into whole and decimal parts
        whole1, dec1 = (num1.split('.') + [''])[:2]
        whole2, dec2 = (num2.split('.') + [''])[:2]

        # Step 1: Add decimal parts
        decimal_sum, carry = self.add_decimal_strings(dec1, dec2)

        # Step 2: Add whole number parts with carry from decimal
        whole_sum, carry2 = self.add_integer_strings(whole1, whole2, carry)

        # Step 3: Include final carry
        if carry2:
            whole_sum = str(carry2) + whole_sum

        # Step 4: Format output
        if decimal_sum.rstrip('0'):  # remove trailing zeros only if meaningful
            return f"{whole_sum}.{decimal_sum.rstrip('0')}"
        else:
            return whole_sum
