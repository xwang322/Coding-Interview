import java.util.*;
/*
 (1)给一个数组求不相邻元素所能组成的最大和; 
 (2)给一个binary tree求
不相邻元素所能组成的最大和。数字都可正可负
*/
//use dp,see in leetcode
//如果是树的话，应该用一个length=2 的数组记录偷或者不偷的钱，第一种，root没偷，最大值等于
//两个孩子最大值之和，第二种偷了，最大值等于root.va+两个孩子没偷的结果
class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;
  public TreeNode(int val) {
    this.val = val;
  }
}

public class Solution {
  
    public static int rob(int[] arr) {
      int[] dp = new int[arr.length+1];
      dp[0] = 0;
      dp[1] = arr[0];
      for(int i=2;i<dp.length;i++) {
        dp[i] = Math.max(dp[i-1], dp[i-2] + arr[i-1]);
      }
      return dp[arr.length];
    }
  
   public static int rob(TreeNode root) {
    int[] res = robSub(root);
    return Math.max(res[0], res[1]);
  }

private static  int[] robSub(TreeNode root) {
    if (root == null) return new int[2];
    
    int[] left = robSub(root.left);
    int[] right = robSub(root.right);
    int[] res = new int[2];

    res[0] = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
    res[1] = root.val + left[0] + right[0];
    
    return res;
}
  
    // Driver program to test the above functions
    public static void main(String args[]) 
    {
        TreeNode root=new TreeNode(8);
        root.left   = new TreeNode(2);
        root.right  = new TreeNode(3);
        root.left.left  = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.right = new TreeNode(8);
        root.right.right.left  = new TreeNode(6);
        root.right.right.right  = new TreeNode(7);
        int[] arr ={1, 1, 2, 3, 5, 6, 9, 2};
        System.out.print(rob(root));
    }


  
}
