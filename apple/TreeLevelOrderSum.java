// tree level-order sum
import java.util.*;
import java.io.*;
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}
class Solution {
    public static void main(String[] args) {
        TreeNode n1 = new TreeNode(3);
        TreeNode n2 = new TreeNode(9);
        TreeNode n3 = new TreeNode(20);
        TreeNode n4 = new TreeNode(15);
        TreeNode n5 = new TreeNode(7);
        n1.left = n2;
        n1.right = n3;
        n3.left = n4;
        n3.right = n5;
        List<Integer> answer = levelOrderSum(n1);
        for (Integer ele : answer) {
            System.out.println(ele);
        }
    }

    public static List<Integer> levelOrderSum(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        List<Integer> answer = new ArrayList<>();
        if (root == null) return answer;
        queue.offer(root);
        while (!queue.isEmpty()) {
            int sublist = 0;
            int subtotal = queue.size();
            for (int i = 0; i < subtotal; i++) {
                TreeNode node = queue.poll();
                sublist += node.val;
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
            answer.add(sublist);
        }
        return answer;
    }
}
