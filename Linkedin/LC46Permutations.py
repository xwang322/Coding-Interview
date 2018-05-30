class Solution(object):
    def permute(self, nums):
        nums.sort()
        answer = []
        n = len(nums)
        self.dfs(nums, answer, [], n)
        return answer

    def dfs(self, nums, answer, path, total):
        if len(path) == total:
            answer.append(path)
        for index, num in enumerate(nums):
            self.dfs(nums[:index]+nums[index+1:], answer, path+[num], total)
