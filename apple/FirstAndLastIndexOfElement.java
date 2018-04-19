/*
找到一个sorted list里面target的最小和最大index
a = [1,2,4,4,4,8], target = 4, return [2,4]
*/
import java.io.*;
import java.util.*;
class Solution {
  public static void main(String[] args) {
      int answer1 = bisect_left(new int[]{1,2,4,4,4,8}, 4);
      int answer2 = bisect_right(new int[]{1,2,4,4,4,8}, 4);
      System.out.println(answer1);
      System.out.println(answer2-1);
  }

  public static int bisect_right(int[] nums, int target) {
      int low = 0;
      int high = nums.length;
      if (nums.length == 0) return 0;
      if (target < nums[low]) return low;
      if (target > nums[high-1]) return high;
      for(;;) {
          if (low+1 == high) return low+1;
          int mid = (low+high)/2;
          if (target < nums[mid]) high = mid;
          else low = mid;
      }
  }

  public static int bisect_left(int[] nums, int target) {
      int low = 0;
      int high = nums.length;
      if (nums.length == 0) return 0;
      if (target < nums[low]) return low;
      if (target > nums[high-1]) return high;
      for(;;) {
          if (low+1 == high) return target == nums[low] ? low:(low+1);
          int mid = (low+high)/2;
          if (target <= nums[mid]) high = mid;
          else low = mid;
      }
  }
}
