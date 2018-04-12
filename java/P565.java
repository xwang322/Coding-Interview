class Solution {
    public int arrayNesting(int[] nums) {
        if (nums.length == 1) return 1;
        int max = 1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != -1) {
                int count = 0;
                int index = i;
                while (nums[index] != -1) {
                    count++;
                    int temp = nums[index];
                    nums[index] = -1;
                    index = temp;
                }
                max = Math.max(max, count);
            }
        }
        return max;
    }
}