class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        temp = 10000
        answer = 0
        for i in range(len(nums)):
            left = i+1; right = len(nums)-1
            while left < right:
                sum = nums[i]+nums[left]+nums[right]
                diff = abs(sum-target)
                if diff < temp:
                    temp = diff
                    answer = sum
                if diff == 0:
                    return sum
                elif sum > target:
                    right -= 1
                else:
                    left += 1
        return answer
        