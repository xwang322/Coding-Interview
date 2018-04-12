class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        start = 0
        answer = 1
        while start <= len(nums)-2:
            if nums[start] != nums[start+1]:
                nums[answer] = nums[start+1]
                answer += 1
            start += 1
        return answer
        