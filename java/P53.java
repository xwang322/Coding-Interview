class Solution {
    public int maxSubArray(int[] nums) {
        return Subarray(nums, 0, nums.length-1);
    }
    
    public int Subarray(int[] A, int left, int right) {
        if (left == right) return A[left];
        int mid = left + (right-left)/2;
        int leftsum = Subarray(A, left, mid);
        int rightsum = Subarray(A, mid+1, right);
        int crosssum = Crossarray(A, left, right);
        if (leftsum >= rightsum && leftsum >= crosssum) return leftsum;
        else if (rightsum >= leftsum && rightsum >= crosssum) return rightsum;
        else return crosssum;
    }
    
    public int Crossarray(int[] A, int left, int right) {
        int leftsum = Integer.MIN_VALUE;
        int rightsum = Integer.MIN_VALUE;
        int sum = 0;
        int mid = left+(right-left)/2;
        for (int i=mid; i >= left; i--) {
            sum = sum + A[i];
            if (leftsum < sum) {
                leftsum = sum;
            }
        }
        sum = 0;
        for (int j=mid+1; j <= right; j++) {
            sum = sum + A[j];
            if (rightsum < sum) {
                rightsum = sum;
            }
        }
        return leftsum+rightsum;
    }
}