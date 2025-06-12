"""
| Metric    | Value           |
| --------- | --------------- |
| **Time**  | O(m + n)        |
| **Space** | O(1) (in-place) |

"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Pointer for the last valid element in nums1
        index_nums1 = m - 1

        # Pointer for the last element in nums2
        index_nums2 = n - 1

        # Pointer for the last position in nums1 (including extra space)
        write_index = m + n - 1

        # Loop as long as there are elements left in nums2 to merge
        while index_nums2 >= 0:
            # If nums1 still has elements, and current nums1 is greater than nums2
            if index_nums1 >= 0 and nums1[index_nums1] > nums2[index_nums2]:
                nums1[write_index] = nums1[index_nums1]  # Copy from nums1
                index_nums1 -= 1  # Move pointer left in nums1
            else:
                nums1[write_index] = nums2[index_nums2]  # Copy from nums2
                index_nums2 -= 1  # Move pointer left in nums2

            write_index -= 1  # Move write pointer left



"""
Another Meta Question on Merge Three Sorted Arrays. 


def merge_three_sorted_arrays(arr1, arr2, arr3):
    i = j = k = 0  # Pointers for each array
    result = []

    while i < len(arr1) or j < len(arr2) or k < len(arr3):
        # Get the current values or "infinite" if out of bounds
        val1 = arr1[i] if i < len(arr1) else float('inf')
        val2 = arr2[j] if j < len(arr2) else float('inf')
        val3 = arr3[k] if k < len(arr3) else float('inf')

        # Find the minimum of the three
        if val1 <= val2 and val1 <= val3:
            result.append(val1)
            i += 1
        elif val2 <= val1 and val2 <= val3:
            result.append(val2)
            j += 1
        else:
            result.append(val3)
            k += 1

    return result


| Metric | Value                              |
| ------ | ---------------------------------- |
| Time   | O(n1 + n2 + n3)                    |
| Space  | O(n1 + n2 + n3) (for result array) |

"""
Got it! From now on:

✅ Comments will be in your native language (typed in English, like Telugu spoken).
✅ Variables will have meaningful names.
✅ Each solution will include time and space complexity details.

Let’s begin with **Alien Dictionary** (Leetcode 269) using both **BFS** and **DFS** Topological Sort in Python, with your 3 preferences applied.

---

### ✅ **Approach 1: BFS (Kahn’s Algorithm)**

```python
from collections import defaultdict, deque
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Character graph ni prepare cheyyali
        char_graph = defaultdict(set)
        char_indegree = {char: 0 for word in words for char in word}

        # Adjacent word pairs ni compare chesi graph edges add cheyyali
        for i in range(len(words) - 1):
            first = words[i]
            second = words[i + 1]
            if len(first) > len(second) and first.startswith(second):
                return ""  # Invalid input case like ["abc", "ab"]
            for c1, c2 in zip(first, second):
                if c1 != c2:
                    if c2 not in char_graph[c1]:
                        char_graph[c1].add(c2)
                        char_indegree[c2] += 1
                    break

        # 0 indegree characters ni queue lo pettadam
        topo_queue = deque([c for c in char_indegree if char_indegree[c] == 0])
        order_result = []

        while topo_queue:
            current = topo_queue.popleft()
            order_result.append(current)

            for neighbor in char_graph[current]:
                char_indegree[neighbor] -= 1
                if char_indegree[neighbor] == 0:
                    topo_queue.append(neighbor)

        # Graph lo cycle undi ante incomplete result untundi
        if len(order_result) < len(char_indegree):
            return ""

        return ''.join(order_result)
```

#### 🧠 Time Complexity:

* `O(N + K)` where `N` is total unique characters and `K` is total edges.

#### 💾 Space Complexity:

* `O(N + K)` for graph and indegree map.

---

### ✅ **Approach 2: DFS-based Topological Sort**

```python
from collections import defaultdict
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Graph ni create cheyyali (directed edge from c1 -> c2)
        char_graph = defaultdict(set)
        visited_status = {}  # -1 = visiting, 1 = visited, 0 = unvisited
        result = []

        # All characters ni initialize cheyyali
        for word in words:
            for char in word:
                visited_status[char] = 0

        # Words ni pairwise compare chesi order lo difference vasthe edge add cheyyali
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    char_graph[c1].add(c2)
                    break

        # DFS function: stack path lo node repeat ayithe cycle untundi
        def dfs(char):
            if visited_status[char] == -1:
                return False  # Cycle detected
            if visited_status[char] == 1:
                return True   # Already processed

            visited_status[char] = -1  # Visiting
            for neighbor in char_graph[char]:
                if not dfs(neighbor):
                    return False

            visited_status[char] = 1  # Visited
            result.append(char)
            return True

        for char in visited_status:
            if visited_status[char] == 0:
                if not dfs(char):
                    return ""

        return ''.join(reversed(result))
```

#### 🧠 Time Complexity:

* `O(N + K)` where `N` = unique chars, `K` = rules (edges)

#### 💾 Space Complexity:

* `O(N + K)` for graph + recursion stack + result

---

Let me know if you'd like dry-run examples, or next you want Course Schedule I and II with similar structure!




Absolutely! Here's the **Course Schedule I** problem (LeetCode 207) solved using **both BFS and DFS**, with:

1. 🔤 Variable names that are meaningful
2. 📝 Comments in your native language (typed in English, like Telugu spoken)
3. ⏱️ Time and Space complexity explained at the end

---

## ✅ Problem: Course Schedule I (Leetcode 207)

You're given `numCourses` and a list of prerequisites, and you need to return **True** if it's possible to finish all courses (i.e., there’s **no cycle** in the graph), or **False** otherwise.

---

### ✅ Approach 1: BFS (Kahn's Algorithm)

```python
from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, totalCourses: int, prerequisites: List[List[int]]) -> bool:
        # Graph ni prepare cheddam: prereq[course] ante course depends on prereq
        courseGraph = defaultdict(list)
        indegree = [0] * totalCourses

        # Graph lo edges and indegree ni build cheyyali
        for course, prereq in prerequisites:
            courseGraph[prereq].append(course)
            indegree[course] += 1

        # Queue lo start cheyyali with all courses having indegree 0 (no prereq)
        courseQueue = deque()
        for course in range(totalCourses):
            if indegree[course] == 0:
                courseQueue.append(course)

        completedCourses = 0

        # Topological sort using BFS
        while courseQueue:
            currentCourse = courseQueue.popleft()
            completedCourses += 1

            # Current course valla depend aina courses ni process cheyyali
            for dependentCourse in courseGraph[currentCourse]:
                indegree[dependentCourse] -= 1
                if indegree[dependentCourse] == 0:
                    courseQueue.append(dependentCourse)

        # Completed courses equal to totalCourses ante cycle ledu
        return completedCourses == totalCourses
```

### 🧠 Time Complexity:

* `O(V + E)` → V = numCourses, E = len(prerequisites)

### 💾 Space Complexity:

* `O(V + E)` → for graph and indegree list

---

### ✅ Approach 2: DFS + Cycle Detection

```python
from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, totalCourses: int, prerequisites: List[List[int]]) -> bool:
        # Directed graph ni build cheyyali
        courseGraph = defaultdict(list)
        for course, prereq in prerequisites:
            courseGraph[prereq].append(course)

        # 0 = unvisited, -1 = visiting, 1 = visited
        courseStatus = [0] * totalCourses

        def hasCycle(course: int) -> bool:
            if courseStatus[course] == -1:
                return True  # Visiting ki malli visit ante cycle undi
            if courseStatus[course] == 1:
                return False  # Already visited and safe

            courseStatus[course] = -1  # Mark as visiting
            for nextCourse in courseGraph[course]:
                if hasCycle(nextCourse):
                    return True

            courseStatus[course] = 1  # Done visiting, mark as safe
            return False

        for course in range(totalCourses):
            if courseStatus[course] == 0:
                if hasCycle(course):
                    return False  # Cycle detected

        return True  # All courses can be finished
```

### 🧠 Time Complexity:

* `O(V + E)` → V = numCourses, E = edges (prerequisites)

### 💾 Space Complexity:

* `O(V + E)` for graph and visited array

---

Let me know if you're ready for **Course Schedule II (LC 210)** — it's very similar but asks to return the **course order**, not just whether it's possible.


Here are **both BFS and DFS solutions** for **Leetcode 210: Course Schedule II** in Python, following your preferred format:

---

### ✅ **Problem Summary**

> You're given `numCourses` and a list of prerequisite pairs. Return **any valid order** in which the courses can be finished. If no such order exists (due to a cycle), return an empty list.

---

## 🔁 BFS Approach (Kahn's Algorithm)

```python
from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Prati course ki depend ayina list ni graph lo store chestunnam
        course_graph = defaultdict(list)
        in_degree = [0] * numCourses  # In-degree ante prerequisite count

        # Prerequisites ni graph and in-degree lo update cheyyadam
        for dest, src in prerequisites:
            course_graph[src].append(dest)
            in_degree[dest] += 1

        # In-degree 0 unna courses ni queue lo petti start cheyyadam
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        course_order = []

        # Topological sort using BFS
        while queue:
            course = queue.popleft()
            course_order.append(course)
            for neighbor in course_graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If cycle exists, ante anni courses ni visit cheyyaledu
        if len(course_order) != numCourses:
            return []
        return course_order
```

### ⏱ Time & Space Complexity

* **Time:** `O(V + E)` → Courses + Prerequisites
* **Space:** `O(V + E)` → Graph + Queue + in-degree list

---

## 🌲 DFS Approach

```python
from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Graph ni prepare cheyyadam
        course_graph = defaultdict(list)
        for dest, src in prerequisites:
            course_graph[src].append(dest)

        # Visited status: 0 = unvisited, 1 = visiting, 2 = visited
        visited = [0] * numCourses
        course_order = []
        is_possible = True  # Cycle detect aithe False cheyyali

        def dfs(course):
            nonlocal is_possible
            if visited[course] == 1:  # Cycle detect ayyindi
                is_possible = False
                return
            if visited[course] == 0:
                visited[course] = 1
                for neighbor in course_graph[course]:
                    dfs(neighbor)
                visited[course] = 2
                course_order.append(course)

        for course in range(numCourses):
            if visited[course] == 0:
                dfs(course)

        return course_order[::-1] if is_possible else []
```

### ⏱ Time & Space Complexity

* **Time:** `O(V + E)`
* **Space:** `O(V + E)` → Graph + Visited list + Recursion stack

---

## 🧠 Which One is Preferred at Meta?

> ✅ **BFS (Kahn’s Algorithm)** is often preferred at Meta for topological sort problems like Course Schedule I & II because:

* It's **iterative** and avoids recursion depth issues.
* It **naturally returns** a topological order.
* Interviewers appreciate **clarity and maintainability** — BFS code tends to be easier to reason about in interviews.

That said, DFS is equally acceptable if well-written with **clear cycle detection** and backtracking.

---

Would you like test cases next or move on to another topological problem (like Alien Dictionary or Parallel Courses)?



