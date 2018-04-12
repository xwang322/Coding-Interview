class Solution(object):
    def thirdMax(self, nums):
        nums = list(set(nums))
        if len(nums) <= 2:
            return max(nums)
        one, two, three = nums.index(min(nums)), nums.index(min(nums)), nums.index(min(nums))
        for i in range(len(nums)):
            if nums[i] > nums[one]:
                three = two
                two = one
                one = i
            elif nums[one] > nums[i] > nums[two]:
                three = two
                two = i
            elif nums[two] > nums[i] > nums[three]:
                three = i
        return nums[three]