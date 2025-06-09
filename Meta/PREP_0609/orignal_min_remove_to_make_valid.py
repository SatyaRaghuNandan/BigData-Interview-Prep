class Solution:
    def minRemoveToMakeValid(self, input_string: str) -> str:
        # Step 1: Valid ga unna parentheses ni forward pass lo collect cheddam
        result_after_first_pass = []
        open_seen = 0   # '(' entha sarlu vachindo count cheyyadam kosam
        balance = 0     # ')' ki match aina '(' count cheyyadam kosam

        for ch in input_string:
            if ch == '(':
                open_seen += 1
                balance += 1  # '(' ochindhi ante oka ')' tarvata ravali
            elif ch == ')':
                if balance == 0:
                    # ')' ki match ayye '(' lekapothe skip cheyyali
                    continue
                balance -= 1  # oka ')' ni valid ga consider chesam
            # valid character ni add cheyyadam
            result_after_first_pass.append(ch)

        # Step 2: Backward lo '(' ekkuva vunte avi remove cheyyali
        final_result = []
        open_to_keep = open_seen - balance  
        # open_seen = total '(' count
        # balance = unmatched '(' count (i.e., avi remove cheyyali)

        for ch in result_after_first_pass:
            if ch == '(':
                if open_to_keep == 0:
                    # extra '(' unte skip cheyyali
                    continue
                open_to_keep -= 1  # valid '(' ni keep cheyyadam
            final_result.append(ch)  # valid character ni add cheyyadam

        return ''.join(final_result)
