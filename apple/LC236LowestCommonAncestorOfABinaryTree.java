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
        Map<TreeNode, TreeNode> hashmap = new HashMap<>();
        hashmap.put(root, null);
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!hashmap.containsKey(p) || !hashmap.containsKey(q)) {
            TreeNode node = queue.poll();
            if (node.left != null) {
                hashmap.put(node.left, node);
                queue.offer(node.left);
            }
            if (node.right != null) {
                hashmap.put(node.right, node);
                queue.offer(node.right);
            }
        }
        Set<TreeNode> answer = new HashSet<>();
        while (p != null) {
            answer.add(p);
            p = hashmap.get(p);
        }
        while (!answer.contains(q)){
            q = hashmap.get(q);
        }
        return q;
    }
}
