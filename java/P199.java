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
    // dfs
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<Integer>();
        if (root == null) {
            return result;
        }
        return dfs(root, result, 0);
    }
    
    private List<Integer> dfs(TreeNode root, List<Integer> result, int height) {
        if (height == result.size()) {
            result.add(root.val);
        }
        if (root.right != null) {
            dfs(root.right, result, height+1);
        }
        if (root.left != null) {
            dfs(root.left, result, height+1);
        }
        return result;
    }
}