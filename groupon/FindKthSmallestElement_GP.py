/*
* find kth smallest number in an array
**/
import heapq
def findKthSmallest(nums, k):
    heap = []
    for i in range(len(nums)):
        if len(heap) < k:
            heapq.heappush(heap, -nums[i])
        else:
            temp = heapq.heappop(heap)
            if temp < -nums[i]:
                heapq.heappush(heap, -nums[i])
            else:
                heapq.heappush(heap, temp)
    answer = -heapq.heappop(heap)
    return answer

answer = findKthSmallest([3,2,1,5,6,4], 4)
print answer
