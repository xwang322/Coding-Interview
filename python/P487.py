class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        prev = -1
        curr = 0
        count = 0
        for num in nums:
            if num == 0:
                prev = curr
                curr = 0
            else:
                curr += 1
            count = max(count, prev+curr+1)
        return count
            
        
        