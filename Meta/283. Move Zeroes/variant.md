Here is the **Python version** of the C++ function `move_zeroes_to_front`, which moves all `0`s **to the front** of the list, preserving the order of non-zero elements.

---

### ✅ Python Code with Telugu Comments

```python
from typing import List

def move_zeroes_to_front(nums: List[int]) -> None:
    # swap_index lo end position nundi start cheddam (ippudu ekkada non-zero values petalo chuddam)
    swap_index = len(nums) - 1

    # Reverse loop: last nunchi first varaku
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] != 0:
            # Non-zero value ni swap_index position ki move cheyyadam
            nums[i], nums[swap_index] = nums[swap_index], nums[i]
            swap_index -= 1
```

---

### 📘 Example

```python
nums = [0, 1, 0, 3, 12, 0]
move_zeroes_to_front(nums)
print(nums)  # Output: [0, 0, 0, 1, 3, 12]
```

---

### 🧪 Edge Case Testing

```python
assert (lambda x: move_zeroes_to_front(x) or x)([0]) == [0]
assert (lambda x: move_zeroes_to_front(x) or x)([]) == []
assert (lambda x: move_zeroes_to_front(x) or x)([0, 0, 3, 4, 5]) == [0, 0, 3, 4, 5]
```

---

### 📊 Time & Space Complexity

| Metric              | Value             |
| ------------------- | ----------------- |
| ⏱ Time Complexity   | `O(n)`            |
| 🧠 Space Complexity | `O(1)` (in-place) |

* We traverse the array once (`O(n)`)
* All operations are in-place, so constant space

---

Let me know if you'd like a version that:

* Returns a **new list** (not in-place)
* Preserves the **relative order of zeroes**
* Is implemented using `stable_partition` style logic
