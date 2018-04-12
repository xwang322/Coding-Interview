class Solution(object):
    def twoSum(self, nums, target):
        if not nums or len(nums) == 1:
            return []
        dictionary = {}
        for index, num in enumerate(nums):
            if target-num not in dictionary:
                dictionary[num] = index
            else:
                return [dictionary[target-num], index]
        return []
