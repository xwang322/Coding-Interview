class Solution(object):
    def findMaxLength(self, nums):
        if not nums:
            return 0
        dictionary = {}
        answer = 0
        count0 = 0
        count1 = 0
        dictionary[0] = 0
        for i in range(1, len(nums)+1):
            if nums[i-1] == 0:
                count0 += 1
            else:
                count1 += 1
            if count0-count1 in dictionary:
                answer = max(answer, i-dictionary[count0-count1])
            else:
                dictionary[count0 - count1] = i
        return answer