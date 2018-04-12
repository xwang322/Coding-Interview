class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        answer = cnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
                answer = max(cnt, answer)
            else:
                cnt = 0
        return answer
        
        