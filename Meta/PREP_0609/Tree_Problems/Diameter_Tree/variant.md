Great! Let's create a **full `main()` function** to:

* Build **N-ary trees**
* Run your `diameter()` function
* Print the results
* Include edge cases and typical examples

---

## ✅ Full Python Script with `main()` and Test Cases

```python
from typing import Optional, List

# ✅ N-ary Tree Node definition
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def diameter(self, root: 'Node') -> int:
        diameter = 0

        def longest_path(node: 'Node') -> int:
            if node is None:
                return 0

            max_height = 0
            second_max_height = 0

            for child in node.children:
                height = longest_path(child)

                if height > max_height:
                    second_max_height = max_height
                    max_height = height
                elif height > second_max_height:
                    second_max_height = height

            nonlocal diameter
            diameter = max(diameter, max_height + second_max_height)

            return max_height + 1

        longest_path(root)
        return diameter

# ✅ Helper function to print tree structure (optional, for clarity)
def print_tree(root: Node, indent: int = 0):
    if not root:
        return
    print("  " * indent + f"Node({root.val})")
    for child in root.children:
        print_tree(child, indent + 1)

# ✅ Main function with test cases
def main():
    sol = Solution()

    # 🧪 Test Case 1: Example with 3 children
    #       1
    #     / | \
    #    2  3  4
    #          \
    #           5
    root1 = Node(1, [
        Node(2),
        Node(3),
        Node(4, [
            Node(5)
        ])
    ])
    print("Test Case 1: Expected Diameter = 3")
    print_tree(root1)
    print("Diameter:", sol.diameter(root1))
    print("-" * 50)

    # 🧪 Test Case 2: Single Node Tree
    root2 = Node(10)
    print("Test Case 2: Single Node → Expected Diameter = 0")
    print_tree(root2)
    print("Diameter:", sol.diameter(root2))
    print("-" * 50)

    # 🧪 Test Case 3: Chain Tree (like linked list)
    # 1 -> 2 -> 3 -> 4 -> 5
    chain = Node(1)
    curr = chain
    for i in range(2, 6):
        new_node = Node(i)
        curr.children = [new_node]
        curr = new_node
    print("Test Case 3: Skewed Tree (Chain) → Expected Diameter = 4")
    print_tree(chain)
    print("Diameter:", sol.diameter(chain))
    print("-" * 50)

    # 🧪 Test Case 4: Wide tree with all leaves
    #      1
    #   / / \ \
    #  2 3  4 5
    wide = Node(1, [Node(2), Node(3), Node(4), Node(5)])
    print("Test Case 4: Wide Tree → Expected Diameter = 2")
    print_tree(wide)
    print("Diameter:", sol.diameter(wide))
    print("-" * 50)

    # 🧪 Test Case 5: Null Tree
    print("Test Case 5: Null Tree → Expected Diameter = 0")
    print("Diameter:", sol.diameter(None))
    print("-" * 50)

if __name__ == "__main__":
    main()
```

---

## ✅ Summary of Test Cases

| Test Case | Tree Description          | Expected Diameter |
| --------- | ------------------------- | ----------------- |
| 1         | Multi-level (3→4→5)       | 3                 |
| 2         | Single node               | 0                 |
| 3         | Chain (linked list style) | 4                 |
| 4         | Wide, shallow tree        | 2                 |
| 5         | Null input                | 0                 |

---

Let me know if you want:

* A visualization of diameter paths
* Convert to Leetcode-compatible input format
* Handle node insertion dynamically

You're building interview muscle the right way! 💪🌲
