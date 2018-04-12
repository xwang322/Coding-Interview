class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> queue = new PriorityQueue<Integer>();
        for (int el : nums) {
            queue.add(el);
            if (queue.size() > k) {
                queue.poll();
            }
        }
        return queue.poll();
    }
}