'''
smallest k elements of array
LC215 mutation
'''
def findKthSmallest(nums, k):
        heap = []
        for i in range(len(nums)):
            if len(heap) < k:
                heapq.heappush(heap, nums[i])
            else:
                temp = heapq.heappop(heap)
                if temp < nums[i]:
                    heapq.heappush(heap, temp)
                else:
                    heapq.heappush(heap, nums[i])
        while len(heap) > 1:
            heapq.heappop(heap)
        answer = heapq.heappop(heap)
        return answer
