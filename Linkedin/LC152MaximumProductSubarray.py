class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0
        n = len(nums)
        maxdp = [0 for i in range(n+1)]
        mindp = [0 for i in range(n+1)]
        answer = float('-inf')
        maxdp[0] = 1
        mindp[0] = 1
        for i in range(n):
            maxdp[i+1] = max(maxdp[i]*nums[i], mindp[i]*nums[i], nums[i])
            mindp[i+1] = min(maxdp[i]*nums[i], mindp[i]*nums[i], nums[i])
            answer = max(maxdp[i+1], answer)
        return answer
