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
    public List<Integer> largestValues(TreeNode root) {
        List<Integer> answer = new ArrayList<Integer>();
        dfs(root, answer, 0);
        return answer;
    }
    
    
    private void dfs(TreeNode root, List<Integer> answer, int d) {
        if (root == null) {
            return;
        }
        if (d == answer.size()) {
            answer.add(root.val);
        }
        else {
            answer.set(d, Math.max(root.val, answer.get(d)));
        }
        dfs(root.left, answer, d+1);
        dfs(root.right, answer, d+1);
    }
}