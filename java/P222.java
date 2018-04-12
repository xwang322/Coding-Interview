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
    public int countNodes(TreeNode root) {
        if (root == null) return 0;
        int left = getheight(root.left);
        int right = getheight(root.right);
        if (left == right) {
            return countNodes(root.right) + (1<<left); // includes the whole left side and the root node total counts
        }
        return countNodes(root.left) + (1<<right);
    }
    
    
    public int getheight(TreeNode n) {
        int height = 0;
        while (n != null) {
            height++;
            n = n.left;
        }
        return height;
    }
}