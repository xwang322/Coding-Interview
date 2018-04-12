class Solution(object):
    def topKFrequent(self, nums, k):
        if not nums:
            return []
        counter = collections.Counter(nums)
        heap = []
        for key in counter:
            if len(heap) < k:
                heapq.heappush(heap, (counter[key], key))
            else:
                temp = heapq.heappop(heap)
                if temp[0] > counter[key]:
                    heapq.heappush(heap, temp)
                else:
                    heapq.heappush(heap, (counter[key], key))
        answer = []
        while heap:
            answer.append(heapq.heappop(heap)[1])
        return answer[::-1]
        
