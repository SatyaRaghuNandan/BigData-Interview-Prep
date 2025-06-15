```python

class Solution:

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def lca(root, target):
            if not root or root in target: # Target is 5 and 1. 
                return root
            
            left = lca(root.left, target)
            right = lca(root.right, target)

            if left and right: # ANte em avutundhi ? What do we need to Expect ? 
                return root
            else:
                return left if left else right
            
        return lca(root, [p, q])


"""
- `if not root => if root == null`: **True**
- `if root => if root != null`: **True**
- `if left => if left != null`: **True**
- `if left and right => is left != null and right != null`: **True**

"""
```
