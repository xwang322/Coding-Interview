class Solution(object):
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        nums.sort()
        dict = {}
        answer = set()
        for p in range(len(nums)):
            for q in range(p+1, len(nums)):
                if nums[p] + nums[q] not in dict:
                    dict[nums[p]+nums[q]] = [(p,q)]
                else:
                    dict[nums[p]+nums[q]].append((p,q))
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                T = target - nums[i] - nums[j]
                if T in dict:
                    for k in dict[T]:
                        if k[0] > j:
                            answer.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))
        return [list(i) for i in answer]
        
        
        
        