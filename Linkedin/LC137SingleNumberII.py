class Solution(object):
    def singleNumber(self, nums):
        answer = 0
        for i in range(32):
            count = 0
            for num in nums:
                if (num>>i)&1:
                    count += 1
            count = count%3
            answer += (count<<i)
        return answer if answer < 2**31 else answer-2**32