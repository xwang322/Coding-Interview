class Solution(object):
    def checkSubarraySum(self, nums, k):
        record = {0: -1}
        total = 0
        for i, num in enumerate(nums):
            total += num
            m = total%k if k else total
            if m not in record:
                record[m] = i
            elif record[m]+1 < i:
                return True
        return False
        