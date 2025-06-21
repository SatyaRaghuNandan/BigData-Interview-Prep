1. Binary Search Problem
2. left < right matrame pettuko.
3. left = mid + 1
4. right = mid
5. return left/right ==> Why ? 


Great question! When designing or testing `findPeakElement` or `findValleyElement`, you must consider **edge cases** to ensure correctness and robustness.

Here are **important edge cases** for both **peak** and **valley** detection:

---

## 🔍 Edge Cases to Consider:

### 1. **Single Element**

```python
nums = [5]
```

* **Peak**: 5 is a peak.
* **Valley**: 5 is also a valley.
  ✅ Should return index `0`.

---

### 2. **Two Elements**

```python
nums = [3, 2]   # Decreasing
nums = [2, 3]   # Increasing
```

* For `[3, 2]`:

  * **Peak**: index `0`
  * **Valley**: index `1`
* For `[2, 3]`:

  * **Peak**: index `1`
  * **Valley**: index `0`

✅ Boundary condition handling is important.

---

### 3. **Strictly Increasing**

```python
nums = [1, 2, 3, 4, 5]
```

* **Peak**: Last element is a peak.
* **Valley**: First element is a valley.

---

### 4. **Strictly Decreasing**

```python
nums = [5, 4, 3, 2, 1]
```

* **Peak**: First element is a peak.
* **Valley**: Last element is a valley.

---

### 5. **Valley in the Middle**

```python
nums = [9, 7, 5, 6, 8]
```

* **Valley**: index `2` (`5`)

---

### 6. **Peak in the Middle**

```python
nums = [1, 3, 7, 5, 2]
```

* **Peak**: index `2` (`7`)

---

### 7. **Flat Elements (Duplicates)**

```python
nums = [2, 2, 2, 2]
```

* ⚠️ No valid peak or valley as per strict definition (`nums[i-1] < nums[i] > nums[i+1]`)
* Some versions may allow equality; be clear about the **problem definition**.
  ✅ Decide: Should `==` be treated as increasing/decreasing or disallowed?

---

### 8. **Multiple Peaks/Valleys**

```python
nums = [1, 3, 1, 3, 1]
```

* Peaks: indices `1`, `3`
* Valleys: indices `0`, `2`, `4`
  ✅ Binary Search will return **any one** depending on implementation.

---

### 9. **Plateau Peaks / Valleys**

```python
nums = [1, 2, 2, 2, 1]
```

* Is `2` considered a peak? Depends on definition:

  * Strict: No (since not greater than both neighbors)
  * Non-strict: Yes (if `>=` used)

---

## ✅ Recommendations

* Test with **lengths 0, 1, 2**.
* Try both **monotonic** and **zigzag** arrays.
* Clarify if **equal neighbors are allowed** (some interviews allow, some don’t).
* Make sure your implementation doesn’t go out of bounds (e.g., accessing `nums[mid+1]` when `mid == n-1`).

---

### 📌 Bonus: Test case set

```python
test_cases = [
    [5],
    [3, 2],
    [2, 3],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [1, 3, 7, 5, 2],
    [9, 7, 5, 6, 8],
    [2, 2, 2, 2],
    [1, 3, 1, 3, 1],
    [1, 2, 2, 2, 1],
]
```

Let me know if you want assertions or test harness code in Python/Java for these cases.






![image](https://github.com/user-attachments/assets/de60ebc7-9a03-4d3b-9323-cabb24ca0951)

