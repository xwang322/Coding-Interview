class Solution {
    public int wiggleMaxLength(int[] nums) {
        if (nums == null) return 0;
        if (nums.length <= 1) return nums.length;
        int increase = 1, decrease = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i-1]) increase = decrease+1;
            else if (nums[i] < nums[i-1]) decrease = increase+1;
        }
        return Math.max(increase, decrease);
    }
}