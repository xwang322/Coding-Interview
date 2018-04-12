class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        if len(nums) == 1 or len(nums) == 2:
            return len(nums)
        answer = 0
        for num in nums:
            if answer < 2 or num != nums[answer-2] or num != nums[answer-1]:
                nums[answer] = num
                answer += 1
        return answer