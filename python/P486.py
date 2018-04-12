class Solution(object):
    def PredictTheWinner(self, nums):
        cache = dict()
        def solve(nums):
            if len(nums) <= 1:
                return sum(nums)
            tnums = tuple(nums)
            if tnums in cache:
                return cache[tnums]
            cache[tnums] = max(nums[0]-solve(nums[1:]), nums[-1]-solve(nums[:-1]))
            return cache[tnums]
        return solve(nums) >= 0            
        