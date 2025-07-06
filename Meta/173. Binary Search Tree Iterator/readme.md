


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class BSTIterator {
     private Stack<TreeNode> stack = new Stack<>();



/* BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
*/
    public BSTIterator(TreeNode root) {
        pushLeft(root); // Push all left nodes to the stack
    }

    // Returns the next smallest element
    public int next() {
        TreeNode node = stack.pop();

        // If node has right subtree, push its left path
        if (node.right != null) {
            pushLeft(node.right);
        }

        return node.val;
    }

    // Returns true if there is a next element
    public boolean hasNext() {
        return !stack.isEmpty();
    }

    // Helper method: Push all left children of a subtree to the stack
    private void pushLeft(TreeNode node) {
        while (node != null) {
            stack.push(node);
            node = node.left;
        }
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */
