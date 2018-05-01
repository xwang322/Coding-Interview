// 给一个bst和一个target，输出小于target的最大值
import java.util.*;
import java.io.*;
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) {
        this.val = x;
    }
}
class Solution {
    public static int[] FindCloestTarget(int target, TreeNode root) {
        if (root == null) return new int[2];
        int[] answer = new int[2];
        answer[0] = helper1(root, Integer.MIN_VALUE, Integer.MAX_VALUE, target);
        answer[1] = helper2(root, Integer.MIN_VALUE, Integer.MAX_VALUE, target);
        return answer;
    }

    public static int helper1(TreeNode node, int lower, int upper, int target) {
        if (node == null) {
            return lower;
        }
        if (node.val >= target) return helper1(node.left, lower, node.val, target);
        else return helper1(node.right, node.val, upper, target);
    }

    public static int helper2(TreeNode node, int lower, int upper, int target) {
        if (node == null) {
            return upper;
        }
        if (node.val >= target) return helper2(node.left, lower, node.val, target);
        else return helper2(node.right, node.val, upper, target);
    }

    public static void main (String[] args) {
        TreeNode t1 = new TreeNode(7);
        TreeNode t2 = new TreeNode(4);
        TreeNode t3 = new TreeNode(8);
        TreeNode t4 = new TreeNode(3);
        TreeNode t5 = new TreeNode(6);
        TreeNode t6 = new TreeNode(9);
        t1.left = t2;
        t1.right = t3;
        t2.left = t4;
        t2.right = t5;
        t3.right = t6;
        int target = 10;
        int[] answer = FindCloestTarget(target, t1);
        int choice = Math.abs(answer[0]-target) < Math.abs(answer[1]-target) ? answer[0] : answer[1];
        System.out.println(choice);
    }
}
