/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isValidBST(TreeNode root) {
        return dfs(root, null, null);
    }

    public boolean dfs(TreeNode node, Integer minimum, Integer maximum) {
        if (node == null) return true;
        if (minimum != null && node.val <= minimum) return false;
        if (maximum != null && node.val >= maximum) return false;
        return dfs(node.left, minimum, node.val) && dfs(node.right, node.val, maximum);
    }
}
