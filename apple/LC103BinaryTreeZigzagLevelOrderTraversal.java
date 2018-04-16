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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> answer = new ArrayList<>();
        if (root == null) return answer;
        Stack<TreeNode> current = new Stack<>();
        current.push(root);
        Stack<TreeNode> next_layer = new Stack<>();
        List<Integer> value_layer = new ArrayList<>();
        boolean flag = true;
        while (!current.isEmpty()) {
            TreeNode node = current.pop();
            value_layer.add(node.val);
            if (flag) {
                if (node.left != null) next_layer.push(node.left);
                if (node.right != null) next_layer.push(node.right);
            }
            else {
                if (node.right != null) next_layer.push(node.right);
                if (node.left != null) next_layer.push(node.left);
            }
            if (current.isEmpty()) {
                current = next_layer;
                answer.add(value_layer);
                next_layer = new Stack<>();
                value_layer = new ArrayList<>();
                flag = !flag;
            }
        }
        return answer;
    }
}
