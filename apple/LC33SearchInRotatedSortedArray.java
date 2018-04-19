class Solution {
    public int search(int[] nums, int target) {
        if (nums.length == 0) return -1;
        int left = 0;
        int right = nums.length-1;
        if (target < nums[left] && target > nums[right]) return -1;
        while (left < right) {
            int mid = (left+right)/2;
            if (nums[mid] <= nums[right]) {
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid+1;
                }else {
                    right = mid;
                }
            }else {
                if (nums[left] <= target && target <= nums[mid]) {
                    right = mid;
                }else {
                    left = mid+1;
                }
            }
        }
        if (nums[left] == target) return left;
        else return -1;
    }
}
