class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        dictionary = {}
        answer = 0
        for num in nums:
            start = end = num
            if num in dictionary:
                continue
            if num+1 not in dictionary and num-1 not in dictionary:
                dictionary[num] = (start, end)
            if num+1 in dictionary:
                end = dictionary[num+1][1]
            if num-1 in dictionary:
                start = dictionary[num-1][0]
            dictionary[num] = dictionary[start] = dictionary[end] = (start, end)
            answer = max(answer, end-start+1)
        return answer
