

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Convert the string to a char array (mutable)
        chars = list(s)
        
        # First Pass: Remove extra ')'
        balance = 0  # balance of '(' and ')'
        for i in range(len(chars)):
            if chars[i] == '(':
                balance += 1
            elif chars[i] == ')':
                if balance == 0:
                    chars[i] = ''  # mark invalid ')'
                else:
                    balance -= 1

        # Second Pass: Remove extra '(' from end
        balance = 0
        for i in range(len(chars) - 1, -1, -1):
            if chars[i] == ')':
                balance += 1
            elif chars[i] == '(':
                if balance == 0:
                    chars[i] = ''  # mark invalid '('
                else:
                    balance -= 1

        return ''.join(chars)



class Solution {
    public String minRemoveToMakeValid(String s) {
        StringBuilder sb = new StringBuilder(s);

        // Step 1: Remove invalid closing ')'
        int balance = 0;
        for (int i = 0; i < sb.length(); i++) {
            char c = sb.charAt(i);
            if (c == '(') {
                balance++;
            } else if (c == ')') {
                if (balance == 0) {
                    sb.setCharAt(i, '*'); // Mark for removal
                } else {
                    balance--;
                }
            }
        }

        // Step 2: Remove invalid opening '(' from the end
        balance = 0;
        for (int i = sb.length() - 1; i >= 0; i--) {
            char c = sb.charAt(i);
            if (c == ')') {
                balance++;
            } else if (c == '(') {
                if (balance == 0) {
                    sb.setCharAt(i, '*'); // Mark for removal
                } else {
                    balance--;
                }
            }
        }

        // Step 3: Build final result by skipping marked chars
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < sb.length(); i++) {
            if (sb.charAt(i) != '*') {
                result.append(sb.charAt(i));
            }
        }

        return result.toString();
    }
}



