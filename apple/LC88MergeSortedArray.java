class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int t1 = m-1;
        int t2 = n-1;
        int total = m+n-1;
        while (t1 >= 0 && t2 >= 0) {
            nums1[total--] = nums1[t1] > nums2[t2] ? nums1[t1--] : nums2[t2--];
        }
        while (t2 >= 0) {
            nums1[total--] = nums2[t2--];
        }
    }
}
