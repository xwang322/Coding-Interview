class Solution(object):
    def checkSubarraySum(self, nums, k):
        if not nums or len(nums) == 1:
            return False
        sum_array = [0]*(len(nums)+1)
        for i, num in enumerate(nums):
            sum_array[i+1] = sum_array[i]+num
        if k == 0:
            if sum_array[-1] == 0:
                return True
            else:
                return False
        for i in range(1, len(sum_array)):
            for j in range(i-1):
                if not (sum_array[i]-sum_array[j])%k:
                    return True
        return False