class Solution {
    public int minPatches(int[] nums, int n) {
        int answer = 0;
        long max = 0;
        int i = 0;
        while (max<n) {
            if (i >= nums.length || nums[i]-1 > max) {
                answer++;
                max += max+1;
            } else {
                max += nums[i];
                i++;
            }
        }
        return answer;
    }
}