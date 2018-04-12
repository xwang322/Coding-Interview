class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        return solvefunction(s, nums);
    }
    
    public int solvefunction(int s, int[] nums) {
        int[] sums = new int[nums.length+1];
        for (int i = 1; i < sums.length; i++) {
            sums[i] = sums[i-1]+nums[i-1];
        }
        int minimum = Integer.MAX_VALUE;
        for (int i = 0; i < sums.length; i++) {
            int end = binarysearch(i+1, sums.length-1, sums[i]+s, sums);
            if (end == sums.length) break;
            if (end-i < minimum) minimum = end-i;
        }
        return minimum == Integer.MAX_VALUE ? 0:minimum;
    }
    
    public int binarysearch(int left, int right, int target, int[] sums) {
        while (left <= right) {
            int mid = left+(right-left)/2;
            if (sums[mid] >= target) right = mid-1;
            else left = mid+1;
        }
        return left;
    }
}