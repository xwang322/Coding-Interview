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
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> answers = new LinkedList<>();
        if (root == null) return answers;
        if (root.left == null && root.right == null) {
            answers.add(root.val + "");
            return answers;
        }
        for (String answer: binaryTreePaths(root.left)) {
            answers.add(root.val+"->"+answer);
        }
        for (String answer: binaryTreePaths(root.right)) {
            answers.add(root.val+"->"+answer);
        }
        return answers;
    }
}