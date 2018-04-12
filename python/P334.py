class Solution(object):
    def increasingTriplet(self, nums):
        find1 = 2147483647
        find2 = 2147483647
        for i in range(len(nums)):
            if nums[i] > find2:
                return True
            elif nums[i] > find1:
                find2 = min(find2, nums[i])
            else:
                find1 = nums[i]
        return False
        