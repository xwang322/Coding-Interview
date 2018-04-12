class Solution {
    public int hIndex(int[] citations) {
        int len = citations.length;
        int left = 0, right = len-1;
        while(left <= right) {
            int mid = left+(right-left)/2;
            if (len-mid > citations[mid]) {
                left = mid+1;
            }
            else {
                right = mid-1;
            }
        }
        return len-left;
    }
}