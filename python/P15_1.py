class Solution(object):
    def threeSum(self, nums):
        sorted = nums.sort()
        answer = []
        for i in range(len(nums)-2):
            if i and nums[i] == nums[i-1]:
                continue
            target = nums[i]*(-1)
            left = i+1; right = len(nums)-1
            while left < right:
                if nums[left] + nums[right] == target:
                    answer.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return answer
        