class Solution(object):
    # better use last element as pivot number, using the first one is very hard to debug
    def triangleNumber(self, nums):
        if not nums:
            return 0
        answer = 0
        nums.sort()
        for i in range(len(nums)-1, 1, -1):
            if nums[i] == 0:
                continue
            left = 0
            right = i-1
            while left < right:
                if nums[left]+nums[right] > nums[i]:
                    answer += right-left
                    right -= 1
                else:
                    left += 1
        return answer
