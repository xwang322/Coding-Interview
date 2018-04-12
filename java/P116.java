/**
 * Definition for binary tree with next pointer.
 * public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */
public class Solution {
    // dfs
    public void connect(TreeLinkNode root) {
        if (root == null) return;
        if (root.left == null && root.right == null) return;
        root.left.next = root.right;
        dfs(root.left);
        dfs(root.right);
    }
    
    private void dfs(TreeLinkNode node) {
        if (node == null || node.left == null || node.right == null) return;
        node.left.next = node.right;
        if (node.next != null) node.right.next = node.next.left;
        dfs(node.left);
        dfs(node.right);
    }
}