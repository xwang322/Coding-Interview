class Solution(object):
    def topKFrequent(self, nums, k):
        counter = collections.Counter(nums)
        heap = []
        for key in counter:
            if len(heap) < k:
                heapq.heappush(heap, (counter[key], key))
            else:
                temp = heapq.heappop(heap)
                if temp[0] < counter[key]:
                    heapq.heappush(heap, (counter[key], key))
                else:
                    heapq.heappush(heap, temp)
        answer = []
        while heap:
            answer.append(heapq.heappop(heap)[1])
        return answer
        
