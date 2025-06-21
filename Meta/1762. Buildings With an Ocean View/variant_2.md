Great! You're working on a smart variant of the **Buildings with Ocean View** problem (inspired by **Leetcode 1762 + Leetcode 42: Trapping Rain Water**).

This version returns all buildings that have an **ocean view to either left or right** — not just one side. Let’s convert the given **C++ implementation** into clean, efficient **Python code** with:

* ✅ **Detailed Telugu comments**
* ✅ Time and Space Complexity

---

## ✅ Python Version with Telugu Comments

```python
from typing import List

class Solution:
    def findBuildingsWithViewOnEitherSide(self, heights: List[int]) -> List[int]:
        n = len(heights)
        if n == 1:
            return [0]  # Oka building unte, adi ocean view building

        left = 0
        right = n - 1

        left_view = [left]      # First building ki left view untundhi
        right_view = [right]    # Last building ki right view untundhi

        left_max = heights[left]
        right_max = heights[right]

        # Two pointers: left nunchi → and right nunchi ←
        while left < right:
            if left_max < right_max:
                # Left pointer ni increment cheyyadam
                left += 1
                if heights[left] > left_max and left < right:
                    left_view.append(left)      # Left view undhi
                    left_max = heights[left]    # Max update cheyyadam
            else:
                # Right pointer ni decrement cheyyadam
                right -= 1
                if heights[right] > right_max and left < right:
                    right_view.append(right)    # Right view undhi
                    right_max = heights[right]

        # Right side view ni reverse cheyyali and final result lo add cheyyali
        return left_view + list(reversed(right_view))


def main():
    sol = Solution()

    test_cases = [
        # ✅ Edge Case 1: Only one building
        ([7], [0]),

        # ✅ Edge Case 2: Two buildings
        ([5, 6], [0, 1]),  # Both ends have views

        # ✅ Edge Case 3: All increasing
        ([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]),

        # ✅ Edge Case 4: All decreasing
        ([5, 4, 3, 2, 1], [0, 1, 2, 3, 4]),

        # ✅ Edge Case 5: Equal heights
        ([3, 3, 3, 3], [0, 3]),  # Only ends can have view

        # ✅ Regular Case: Peaks in the middle
        ([2, 4, 3, 5, 1], [0, 1, 3, 4]),

        # ✅ Regular Case: Multiple ups and downs
        ([4, 2, 3, 1, 5], [0, 2, 4]),

        # ✅ Edge Case: Same building heights except one
        ([1, 1, 10, 1, 1], [0, 2, 4]),

        # ✅ Edge Case: Valley in the middle
        ([5, 1, 5], [0, 2]),

        # ✅ Large peak at the end
        ([1, 2, 3, 2, 10], [0, 1, 2, 4])
    ]

    for idx, (heights, expected) in enumerate(test_cases, 1):
        output = sol.findBuildingsWithViewOnEitherSide(heights)
        print(f"Test Case {idx}: heights = {heights}")
        print(f"Expected     : {expected}")
        print(f"Output       : {output}")
        print(f"✅ Pass       : {output == expected}\n")

if __name__ == "__main__":
    main()
```

---

## 🧠 Telugu Explanation (Line-by-Line)

```text
1. oka building matrame unte — adi ocean view building kabatti return [0].

2. left_view = [0], right_view = [n - 1]:
   - First and last buildings ki left/right view untundhi by default.

3. left_max and right_max lo initial max heights ni store chestunnam.

4. while left < right:
   - Two pointers run cheyyadam: oka pointer left nunchi →, inkoti right nunchi ←

5. heights[left] > left_max:
   - Left direction lo ocean view kanipinchindi, so add to left_view

6. heights[right] > right_max:
   - Right direction lo ocean view kanipinchindi, so add to right_view

7. Final ga: left_view + reversed(right_view) return cheyyadam
   - Indices ascending order lo vastayi
```

---

## ⏱ Time and Space Complexity

| Metric           | Complexity | Explanation                                 |
| ---------------- | ---------- | ------------------------------------------- |
| Time Complexity  | `O(N)`     | Each index processed once (left/right)      |
| Space Complexity | `O(N)`     | In worst case, all indices stored in result |

---

## ✅ Sample Input & Output

### Input:

```python
[1, 4, 3, 9, 8, 6]
```

### Output:

```python
[0, 1, 3, 4, 5]
```

---

Let me know if you want a **graphical illustration of views**, or to extend this to also return:

* Only **left view**
* Only **right view**
* Or use this for **water trapping detection** as a next step.
