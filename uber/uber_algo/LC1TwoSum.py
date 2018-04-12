class Solution(object):
    def twoSum(self, nums, target):
        dictionary = {}
        for index, num in enumerate(nums):
            if num not in dictionary:
                dictionary[target-num] = index
            else:
                return [dictionary[num], index]