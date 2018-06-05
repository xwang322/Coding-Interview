class Solution(object):
    def singleNumber(self, nums):
        a = 0
        b = 0
        answer = 0
        for num in nums:
            answer ^= num
        mask = 1
        while answer&mask == 0:
            mask <<= 1
        for num in nums:
            if num&mask:
                a ^= num
            else:
                b ^= num
        return [a,b]