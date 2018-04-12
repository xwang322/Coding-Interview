class Solution(object):
    def twoSum(self, nums, target):
        if not nums or len(nums)<2:
            return []
        dictionary = {}
        for i in range(len(nums)):
            if  target-nums[i] in dictionary:
                return [dictionary[target-nums[i]], i]
            else:
                dictionary[nums[i]] = i
        return []