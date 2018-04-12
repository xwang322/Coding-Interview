class Solution(object):
    def findPairs(self, nums, k):
        if k == 0:
            return sum(v > 1 for v in collections.Counter(nums).values())
        elif k > 0:
            return len(set(nums) & set(n+k for n in nums))
        else:
            return 0
                
                
            
            
        