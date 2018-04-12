class Solution(object):
    def findKthLargest(self, nums, k):
        ''' direct method
        return sorted(nums)[::-1][k-1]        
        '''
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for i in range(len(nums)-k+1):
            element = heapq.heappop(heap)
        return element