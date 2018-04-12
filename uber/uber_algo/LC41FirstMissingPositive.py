class Solution(object):
    def firstMissingPositive(self, nums):
        nums.append(0)
        n = len(nums)
        for i in range(n):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for index, num in enumerate(nums):
            nums[num%n] += n
        for i in range(1, n):
            if nums[i] < n:
                return i
        return n
