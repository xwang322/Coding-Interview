class Solution(object):
    def findRelativeRanks(self, nums):
        lists = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        nums_temp = {u:i for i, u in enumerate(sorted(nums, reverse = True))}
        answer = ['' for i in range(len(nums))]
        for i, num in enumerate(nums):
            if nums_temp[num] >= 3:
                answer[i] = str(nums_temp[num]+1)
            else:
                answer[i] = lists[nums_temp[num]]
        return answer
        