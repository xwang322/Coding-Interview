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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        Map<TreeNode, TreeNode> map = new HashMap<>();
        Deque<TreeNode> stack = new ArrayDeque<>();
        map.put(root, null);
        stack.push(root);
        
        while(!map.containsKey(p) || !map.containsKey(q)) {
            TreeNode node = stack.pop();
            if (node.left != null) {
                map.put(node.left, node);
                stack.push(node.left);
            }
            if (node.right != null) {
                map.put(node.right, node);
                stack.push(node.right);
            }
        }
        Set<TreeNode> path = new HashSet<>();
        while (p != null) {
            path.add(p);
            p = map.get(p);
        }
        while (!path.contains(q)) {
            q = map.get(q);
        }
        return q;
    }
}