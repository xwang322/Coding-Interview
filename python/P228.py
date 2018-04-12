class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        answer = []
        i = 0
        start = 0
        while i < len(nums)-1:
            if nums[i]+1 != nums[i+1]:
                answer.append(self.closerange(nums[start], nums[i]))
                start = i+1
            i += 1
        answer.append(self.closerange(nums[start], nums[i]))
        return answer
    
    def closerange(self, l, r):
        if l == r:
            return str(l)
        else:
            return str(l)+"->"+str(r)