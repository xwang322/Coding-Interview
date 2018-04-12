class Solution(object):
    def threeSumClosest(self, nums, target):
        if not nums:
            return []
        nums.sort()
        answer = float('inf')
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[i]+nums[j]+nums[k] == target:
                    return target
                elif abs(nums[i]+nums[j]+nums[k]-target) < abs(answer-target):
                    answer = nums[i]+nums[j]+nums[k]
                elif nums[i]+nums[j]+nums[k] > target:
                    k -= 1
                else:
                    j += 1
        return answer
            
