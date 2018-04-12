class Solution {
    /*
    public int findPeakElement(int[] nums) {
        for(int i = 1; i <nums.length; i++) {
            if (nums[i]<nums[i-1]) return i-1;
        }
        return nums.length-1;
    */
    // write another method here in Java
    public int findPeakElement(int[] nums) {
        return BS(nums, 0, nums.length-1);
    }
    
    public int BS(int[] nums, int start, int end) {
        if (start == end) return start;
        if (start+1 == end) return nums[start]>nums[end] ? start : end;
        int mid = start + (end-start)/2;
        if (nums[mid] < nums[mid-1]) {
            return BS(nums, start, mid-1);
        }
        if (nums[mid] < nums[mid+1]) {
            return BS(nums, mid+1, end);
        }
        return mid;
    }
}