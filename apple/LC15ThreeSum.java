class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> answer = new ArrayList<>();
        if (nums.length < 3) return answer;
        Arrays.sort(nums);
        for(int i = 0; i < nums.length-2; i++) {
            if (i > 0 && nums[i-1] == nums[i]) continue;
            for (int j = i+1, k = nums.length-1; j<k;) {
                if (nums[i]+nums[j]+nums[k] == 0) {
                    answer.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    j++;
                    k--;
                    while (j<k && nums[j-1] == nums[j]) j++;
                    while (j<k && nums[k+1] == nums[k]) k--;
                }else if (nums[i]+nums[j]+nums[k] > 0) {
                    k--;
                }
                else{
                    j++;
                }
            }
        }
        return answer;
    }
}


// printable version on Coderpad
import java.io.*;
import java.util.*;
class Solution {
  public static void main(String[] args) {
      List<List<Integer>> ans = threeSum(new int[]{-1, 0, 1, 2, -1, -4});
      for (List<Integer> row: ans) {
          System.out.println(row);
      }
  }

  public static List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> answer = new ArrayList<>();
        if (nums.length < 3) return answer;
        Arrays.sort(nums);
        for(int i = 0; i < nums.length-2; i++) {
            if (i > 0 && nums[i-1] == nums[i]) continue;
            for (int j = i+1, k = nums.length-1; j<k;) {
                if (nums[i]+nums[j]+nums[k] == 0) {
                    answer.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    j++;
                    k--;
                    while (j<k && nums[j-1] == nums[j]) j++;
                    while (j<k && nums[k+1] == nums[k]) k--;
                }else if (nums[i]+nums[j]+nums[k] > 0) {
                    k--;
                }
                else{
                    j++;
                }
            }
        }
        return answer;
    }
}
