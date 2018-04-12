class Solution(object):
    '''BT method
    def subsets(self, nums):
        if not nums:
            return []
        answer = []
        nums.sort()
        self.dfs(nums, answer, [], 0)
        return answer
        
    def dfs(self, nums, answer, path, index):
        answer.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, answer, path+[nums[i]], i+1)
    '''
    # Bit Manipulation method
    def subsets(self, nums):
        nums.sort()
        total = 1<<len(nums)
        answer = []
        for i in range(total):
            temp = []
            for j in range(len(nums)):
                if i>>j & 1:
                    temp.append(nums[j])
            answer.append(temp)
        return answer
        
                