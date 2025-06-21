Great! This variant — `previousPermutation()` — is the **mirror opposite** of `nextPermutation()`. It computes the **previous lexicographical permutation** in-place.

Let’s help you remember this using a **mirror version of the V-S-R pattern** from earlier.

---

## 🧠 High-Level Intuition

You want to **step back** from the current permutation and find the one that’s **just smaller**. If the current permutation is the **lowest possible** (sorted ascending), you wrap around to the **highest permutation** (sorted descending).

---

## ✅ Memory Framework: “**P-S-R**”

(Like: **Peak, Swap, Reverse** — mirror of Valley-Swap-Reverse)

| Step | Name        | What to Do                                              | Why?                        |
| ---- | ----------- | ------------------------------------------------------- | --------------------------- |
| 1️⃣  | **P**eak    | Find the first element going *up* from the end          | This is where we step back  |
| 2️⃣  | **S**wap    | Find the largest element smaller than the peak and swap | To make it just smaller     |
| 3️⃣  | **R**everse | Reverse the suffix to get largest possible ending       | To stay closest to original |

---

## 🧩 Detailed Steps

### 🔹 Step 1: **Find the Peak**

```python
for i in range(len(nums) - 1, 0, -1):
    if nums[i - 1] > nums[i]:
        peak = i - 1
        break
```

* Scan from right to left
* Find the first index `peak` where `nums[peak] > nums[peak + 1]`
* This is where we can **make the permutation smaller**

If not found:
Array is already smallest → reverse to get largest.

---

### 🔹 Step 2: **Find the Next Smaller**

```python
next_lower = len(nums) - 1
while nums[next_lower] >= nums[peak]:
    next_lower -= 1
```

* From the right, find the **largest number smaller than `nums[peak]`**
* This ensures we step back **just one permutation**

---

### 🔹 Step 3: **Swap and Reverse**

```python
nums[peak], nums[next_lower] = nums[next_lower], nums[peak]
```

* Swap them to move to the previous configuration

```python
left = peak + 1
right = len(nums) - 1
while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1
```

* Reverse the suffix (right of peak) to get the **largest** possible number from that suffix

---

## 🧠 Mnemonic for Previous Permutation:

> "**P-S-R** → Peak, Swap, Reverse"

Think of it as the **backward twin** of `nextPermutation`’s **V-S-R**.

---

## ✅ Interview Summary to Say:

> “To find the previous permutation, I look for the first increasing pair from the right — that’s my `peak`. I then find the largest number to its right that’s still smaller and swap them. Then I reverse the suffix to get the largest possible arrangement smaller than the current one. If no such `peak` exists, I reverse the entire array because it’s already the smallest permutation.”

---

## 💡 Side-by-Side Summary

|          | `nextPermutation()`              | `previousPermutation()`          |
| -------- | -------------------------------- | -------------------------------- |
| Trigger  | Find `nums[i-1] < nums[i]`       | Find `nums[i-1] > nums[i]`       |
| Find     | Just larger → `>` comparison     | Just smaller → `<` comparison    |
| Reverse  | Make suffix smallest (ascending) | Make suffix largest (descending) |
| Mnemonic | Valley → Swap → Reverse (VSR)    | Peak → Swap → Reverse (PSR)      |

---

Let me know if you want this as a **printable cheat sheet** or with **example dry runs**!
