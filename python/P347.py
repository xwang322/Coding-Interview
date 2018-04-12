class Solution(object):
    def topKFrequent(self, nums, k):
        count_dict = collections.Counter(nums)
        heap = []
        for key in count_dict:
            heapq.heappush(heap, (-count_dict[key], key))
        answer = []
        for i in range(k):
            answer.append(heapq.heappop(heap)[1])
        return answer
        