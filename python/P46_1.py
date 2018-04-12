class Solution(object):
    ''' not working because of bracket layer
    def permute(self, nums):
        if len(nums) == 1:
            return [[nums[0]]]
        answer = []
        for i in range(len(nums)):
            print self.recursive(nums[i], nums[:i]+nums[i+1:])
            answer.append(self.recursive(nums[i], nums[:i]+nums[i+1:])) 
        return answer
        
    def recursive(self, num, restnums):
        if len(restnums) == 0:
            return []
        else:
            answer = []
            for i in range(len(restnums)):
                temp = [num] + self.recursive(restnums[i], restnums[:i]+restnums[i+1:]) 
                answer.append(temp)
            return answer
    # this is the second best
    def permute(self, nums):
        answer = [nums]
        for i in range(len(nums)-1):
            for each in answer[:]:
                for j in range(i+1, len(nums)):
                    answer.append(each[:i]+each[j:]+each[i:j])
        return answer
    ''' 
    #this is the best
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]
        answer = []
        for index, num in enumerate(nums):
            answer += [[num]+p for p in self.permute(nums[:index]+nums[index+1:])]
        return answer