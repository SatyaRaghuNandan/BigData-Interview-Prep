Here is the **Python version** of your `moveZeroes` C++ code, along with:

* ✅ Equivalent logic
* 💬 Detailed Telugu comments
* 📊 Time and Space Complexity analysis

---

## ✅ Python Code with Telugu Comments

```python
from typing import List

def moveZeroes(nums: List[int]) -> None:
    # swap_index ane variable non-zero element ni yekkada petali ani indicate chestundi
    swap_index = 0

    # array lo prathi element ni oka sari choodadam
    for i in range(len(nums)):
        if nums[i] != 0:
            # non-zero element dorikite, current position (i) to swap_index ni swap cheyyadam
            nums[i], nums[swap_index] = nums[swap_index], nums[i]
            # taruvata next non-zero element ki place update cheyyadam
            swap_index += 1
```

---

## 📘 Example

```python
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
```

---

## 📊 Time & Space Complexity

| Metric              | Value             |
| ------------------- | ----------------- |
| ⏱ Time Complexity   | `O(n)`            |
| 🧠 Space Complexity | `O(1)` (in-place) |

* We traverse the list only once (`O(n)`)
* No extra memory used — in-place swaps

---

Let me know if you want:

* 🧪 Unit tests
* 🚀 Optimization ideas
* 🔁 Version using `pop` and `append` instead of `swap`
