class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        if (nums == null) return 0;
        int answer = 0;
        int left = 0;
        int numberofzeros = 0;
        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == 0) {
                numberofzeros++;
            }
            while (numberofzeros == 2) {
                if (nums[left] == 0){
                    numberofzeros--;
                }
                left++;
            }
            answer = Math.max(answer, right-left+1);
        }
        return answer;
    }
}