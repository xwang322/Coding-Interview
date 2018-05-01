class Solution {
    public boolean canJump(int[] nums) {
        if (nums == null  || nums.length == 0) return true;
        int answer = nums.length-1;
        for (int i = nums.length-1; i>= 0; i--) {
            if (nums[i] + i >= answer) {
                answer = i;
            }
        }
        return answer == 0;
    }
}
