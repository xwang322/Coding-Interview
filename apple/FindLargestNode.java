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
    public static int FindLargestTarget(int target, TreeNode root) {
        if (root == null) return Integer.MIN_VALUE;
        return helper(root, Integer.MIN_VALUE, Integer.MAX_VALUE, target);
    }

    public static int helper(TreeNode node, int lower, int upper, int target) {
        if (node == null) {
            return lower;
        }
        if (node.val >= target) return helper(node.left, lower, node.val, target);
        else return helper(node.right, node.val, upper, target);
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
        int answer = FindLargestTarget(target, t1);
        System.out.println(answer);
    }
}
