class Solution(object):
    def findKthLargest(self, nums, k):
        if not nums:
            return None
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        return heapq.heappop(heap)