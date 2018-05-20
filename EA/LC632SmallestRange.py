'''
Smallest Window 给一些windows, 输出smallest window要求cover到每一个window
Input: [4, 10, 15, 23, 26], [0, 9, 12, 19], [5, 18, 22, 30]
Output: [19, 23]
'''

class Solution(object):
    def smallestRange(self, nums):
        if not nums:
            return []
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
        answer = [-float('inf'), float('inf')]
        tempmax = max(num[0] for num in nums)
        while heap:
            num, row, index = heapq.heappop(heap)
            if tempmax-num < answer[1]-answer[0]:
                answer[0] = num
                answer[1] = tempmax
            if index+1 == len(nums[row]):
                return answer
            tempmax = max(tempmax, nums[row][index+1])
            heapq.heappush(heap, (nums[row][index+1], row, index+1))

    '''
    def smallestRange(self, nums):
        pq = [(subnums[0], i, 0) for i, subnums in enumerate(nums)]
        heapq.heapify(pq)
        answer = [-100000, 100000]
        right = max(subnum[0] for subnum in nums)
        while pq:
            num, row, index = heapq.heappop(pq)
            if right-num < answer[1]-answer[0]:
                answer[1] = right
                answer[0] = num
            if len(nums[row]) == index+1:
                return answer
            right = max(right, nums[row][index+1])
            heapq.heappush(pq, (nums[row][index+1], row, index+1))
    '''
    '''
    def smallestRange(self, nums):
        map1 = collections.defaultdict(set)
        map2 = collections.defaultdict(set)
        nsize = len(nums)
        for idx, nlist in enumerate(nums):
            for each in nlist:
                map1[each].add(idx)
        snum = sorted(set(n for nlist in nums for n in nlist))
        snum_size = len(snum)

        start = end = 0
        answer = [snum[0], snum[-1]]
        gap = 0xffffff
        while start < snum_size and end < snum_size:
            while end < snum_size and len(map2) < nsize:
                for each in map1[snum[end]]:
                    map2[each].add(snum[end])
                end += 1
            while start < snum_size and len(map2) == nsize:
                if len(map2) == nsize and snum[end-1] - snum[start] < gap:
                    gap = snum[end-1] - snum[start]
                    answer = [snum[start], snum[end-1]]
                for each in map1[snum[start]]:
                    map2[each].remove(snum[start])
                    if not map2[each]:
                        del map2[each]
                start += 1
        return answer
    '''
