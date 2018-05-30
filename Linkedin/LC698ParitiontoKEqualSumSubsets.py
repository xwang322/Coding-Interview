class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)
        if total%k:
            return False
        visited = [0 for i in range(len(nums))]
        return self.dfs(nums, total/k, k, visited, 0, 0)

    def dfs(self, nums, target, groups, visited, current, index):
        if groups == 1 and current == target:
            return True
        elif current == target:
            return self.dfs(nums, target, groups-1, visited, 0, 0)
        else:
            for i in range(index, len(nums)):
                if nums[i] + current <= target and not visited[i]:
                    visited[i] = 1
                    if self.dfs(nums, target, groups, visited, current+nums[i], i+1):
                        return True
                    visited[i] = 0
            return False
            
