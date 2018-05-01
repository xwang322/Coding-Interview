// binary search，真的就是找一个sorted array里面有没有target
import java.util.*;
import java.io.*;
class Solution {
    public static boolean BinarySearch(int[] nums, int target) {
        if (nums == null || nums.length == 0) return false;
        int left = 0;
        int right = nums.length-1;
        while (left <= right) {
            int middle = left + (right-left)/2;
            if (nums[middle] == target) return true;
            else if (nums[middle] > target) right = middle-1;
            else left = middle+1;
        }
        return false;
    }

    public static void main (String[] args) {
        int target = 10;
        int[] nums = new int[]{1,3,4,6,7,9};
        boolean answer = BinarySearch(nums, target);
        System.out.println(answer);
    }
}
