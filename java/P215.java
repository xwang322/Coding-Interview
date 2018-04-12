class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(k+1);
        for (int num:nums) {
            pq.offer(num);
            if (pq.size() == k+1) {
                pq.poll();
            }
        }
        return pq.poll();
    }
}