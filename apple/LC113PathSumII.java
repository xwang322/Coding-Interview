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
    public List<List<Integer>> answer = new ArrayList<>();
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        if (root == null) return answer;
        Stack<Integer> path = new Stack<>();
        dfs(root, path, sum);
        return answer;
    }

    public void dfs(TreeNode root, Stack<Integer> path, int sum) {
        path.push(root.val);
        if (root.left == null && root.right == null) {
            if (sum == root.val) {
                answer.add(new ArrayList<>(path));
            }
        }
        if (root.left != null) dfs(root.left, path, sum-root.val);
        if (root.right != null) dfs(root.right, path, sum-root.val);
        path.pop();
    }
}
