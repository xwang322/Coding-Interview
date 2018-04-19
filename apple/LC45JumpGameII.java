class Solution {
    public int jump(int[] nums) {
        if (nums.length == 0 || nums == null) return 0;
        int start = 0;
        int end = 0;
        int answer = 0;
        while (end < nums.length-1) {
            answer++;
            int currentend = end+1;
            for (int i = start; i < end+1; i++) {
                if (i + nums[i] >= nums.length -1) return answer;
                currentend = Math.max(currentend, i+nums[i]);
            }
            start = end;
            end = currentend;
        }
        return answer;
    }
}
