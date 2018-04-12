class Solution(object):
    def totalHammingDistance(self, nums):
        if not nums:
            return 0
        answer = 0
        for i in range(32):
            count0 = 0
            count1 = 0
            for num in nums:
                if (num>>i)&1:
                    count1 += 1
                else:
                    count0 += 1
            answer += count0*count1
        return answer