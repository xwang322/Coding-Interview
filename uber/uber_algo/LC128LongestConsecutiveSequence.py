class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        dictionary = {}
        length = 1
        for num in nums:
            start = end = num
            if num in dictionary:
                continue
            if num-1 not in dictionary and num+1 not in dictionary:
                dictionary[num] = (start, end)
            if num+1 in dictionary:
                end = dictionary[num+1][1]
            if num-1 in dictionary:
                start = dictionary[num-1][0]
            dictionary[start] = dictionary[end] = dictionary[num] = (start, end)
            length = max(length, end-start+1)
        return length
