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
class Solution {
    // Post Order Traversal. 
    /** Root Right and Left */
    private double max;
    public double maximumAverageSubtree(TreeNode root) {
       dfs(root, 0);
       return max;
    }

    private int[] dfs(TreeNode node, int previousSum) { // Here is the Tracker.
        if (node == null) {
            return new int[] {0, 0};
        }

        int currentSum = previousSum + node.val;
        int[] left = dfs(node.left, currentSum);
        int[] right = dfs(node.right, currentSum);
        int totalSum = left[0] + right[0] + node.val;
        int totalCount = left[1] + right[1] + 1; // Why Diameter Question has the same thing.s 
        max = Math.max(max, (double) totalSum/ totalCount);
        return new int[] {totalSum, totalCount};
    }
}
