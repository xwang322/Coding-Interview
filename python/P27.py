class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0
        if len(nums) == 1 and nums[0] == val:
            return 0
        elif len(nums) == 1 and nums[0] != val:
            return 1
        start = 0
        answer = 0
        while start <= len(nums)-1:
            if nums[start] != val:
                nums[answer] = nums[start]
                answer += 1
            start += 1
        return answer
        