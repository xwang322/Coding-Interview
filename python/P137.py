class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for i in range(32):
            count = 0
            for num in nums:
                count += (num>>i)&1
            rem = count%3
            if rem and i==31:
                result -= 1<<31
            else:
                result |= rem<<i
        return result