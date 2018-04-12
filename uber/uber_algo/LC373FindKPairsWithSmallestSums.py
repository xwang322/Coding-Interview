class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2:
            return []
        heap = []
        for num1 in nums1:
            for num2 in nums2:
                if len(heap) < k:
                    heapq.heappush(heap, (-num1-num2, [num1, num2]))
                else:
                    if heap and -heap[0][0] > num1+num2:
                        heapq.heappop(heap)
                        heapq.heappush(heap, (-num1-num2, [num1, num2]))
        return [heapq.heappop(heap)[1] for i in range(k) if heap]   
        