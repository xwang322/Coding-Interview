class Solution(object):
    def matrixReshape(self, nums, r, c):
        m = len(nums)
        n = len(nums[0])
        if m*n != r*c:
            return nums
        answer = []
        candidate = reduce(lambda x, y: x+y, nums)
        k = 0
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(candidate[k])
                k += 1
            answer.append(temp)
        return answer
        
