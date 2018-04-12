class Solution(object):
    def findKthLargest(self, nums, k):
        heap = []
        for i in range(len(nums)):
            if len(heap) < k:
                heapq.heappush(heap, nums[i])
            else:
                temp = heapq.heappop(heap)
                if temp > nums[i]:
                    heapq.heappush(heap, temp)
                else:
                    heapq.heappush(heap, nums[i])
        answer = heapq.heappop(heap)
        return answer
