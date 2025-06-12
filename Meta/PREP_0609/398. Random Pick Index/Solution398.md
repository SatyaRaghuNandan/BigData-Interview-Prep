You're sharing a C++ implementation of **LeetCode 398: Random Pick Index**, where the goal is to:

> Given an integer array with possible duplicates, randomly return the **index** of a given `target` number such that each index has **equal probability** of being returned.

---

### ✅ Problem Strategy

This solution precomputes a mapping of each number → all indices where it appears. Then, to pick an index for a target:

1. Get the list of indices from the map.
2. Pick one at **random** using `rand() % size`.

---

## ✅ Python Version with Detailed Telugu Comments

```python
import random
from collections import defaultdict

class Solution398:
    def __init__(self, nums: list[int]):
        # num_to_indices lo prathi number ki tana indices ni list ga map cheddam
        self.num_to_indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.num_to_indices[num].append(i)

    def pick(self, target: int) -> int:
        # Target number ki corresponding indices list ni fetch cheyyadam
        indices = self.num_to_indices[target]
        # Random ga oka index pick cheyyadam
        return random.choice(indices)
```

---

### 🧪 Example

```python
solution = Solution398([1, 2, 3, 3, 3])
print(solution.pick(3))  # Output: Randomly one of [2, 3, 4]
print(solution.pick(1))  # Output: 0
```

Each index has equal probability. If `3` occurs at `[2, 3, 4]`, each index should be picked \~33% of the time over many calls.

---

### ⏱️ Time & Space Complexity

| Method         | Time Complexity | Space Complexity                              |
| -------------- | --------------- | --------------------------------------------- |
| `__init__`     | `O(n)`          | `O(n)`                                        |
| `pick(target)` | `O(1)`          | `O(1)`           (for lookup and random pick) |

---

### ✅ Summary

| Feature                  | ✅ Implemented |
| ------------------------ | ------------- |
| Handles duplicates       | ✅             |
| Uniform random selection | ✅             |
| Preprocessed for speed   | ✅             |

---

Would you like a **space-optimized version using Reservoir Sampling**, which doesn't store all indices in memory? That works better for **large streams**.
