def remove_all_adjacent_1(s: str) -> str:
    i = 0
    res = []

    while i < len(s):
        if not res or res[-1] != s[i]:
            res.append(s[i])
            i += 1
        else:
            # Skip all consecutive duplicates
            while i < len(s) and s[i] == res[-1]:
                i += 1
            res.pop()  # Remove the last one that matched
    return ''.join(res)



def remove_all_adjacent_2(s: str) -> str:
    res = []

    i = 0
    while i < len(s):
        if not res or s[i] != res[-1]:
            res.append(s[i])
            i += 1
        else:
            # Skip the whole group of duplicates
            while i < len(s) - 1 and s[i] == s[i + 1]:
                i += 1
            i += 1  # Move past the last duplicate
            res.pop()  # Remove the last pushed character
    return ''.join(res)



test_cases = [
    ("azxxxzy", "ay"),
    ("abbaxx", ""),
    ("aabbaaac", "c"),
    ("abccba", ""),
    ("abcddcba", ""),
    ("abcdefg", "abcdefg"),
]

for func in [remove_all_adjacent_1, remove_all_adjacent_2]:
    print(f"Testing {func.__name__}")
    for s, expected in test_cases:
        result = func(s)
        print(f"Input: {s}, Output: {result}, Pass: {result == expected}")
    print()



class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = []
        for c in s:
            if result and result[-1] == c: # If the Chars are Same.
                result.pop()
            else:
                result.append(c)
        return "".join(result)




class Solution:
	def removeDuplicates(self, input: str, k : int) -> str:
		stack = []
		
		for ch in input:
			if stack and stack[-1][0] == ch:
				stack[-1][1] += 1 # As we are incrementing the we can check if the number == k
				if stack[-1][1] == k:
					stack.pop()
			else:
				stack.append([ch, 1])
				
		return "".join([s * count for s, count in stack])

