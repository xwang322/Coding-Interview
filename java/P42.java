class Solution {
    public int trap(int[] height) {
        if (height.length <= 2) return 0;
        int answer = 0;
        int max = Integer.MIN_VALUE;
        int maxindex = -1;
        for(int i = 0; i < height.length; i++) {
            if(height[i] > max) {
                max = height[i];
                maxindex = i;
            }
        }
        int leftmax = height[0];
        for (int i = 0; i < maxindex; i++) {
            if (height[i] > leftmax) {
                leftmax = height[i];
            }
            else {
                answer += leftmax-height[i];
            }
        }
        int rightmax = height[height.length-1];
        for (int i = height.length-1; i > maxindex; i--) {
            if (height[i] > rightmax) {
                rightmax = height[i];
            }
            else {
                answer += rightmax-height[i];
            }
        }
        return answer;
    }
}