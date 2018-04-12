class Solution(object):
    #binary search
    def splitArray(self, nums, m):
        largest = max(nums)
        overall = sum(nums)
        while largest < overall:
            mid = (largest+overall)/2
            if self.can_split(nums, m, mid):
                overall = mid
            else:
                largest = mid+1
        return largest
    
    def can_split(self, nums, m, target):
        count = 1
        sum_cur = 0
        for num in nums:
            sum_cur += num
            if sum_cur > target:
                sum_cur = num
                count += 1
                if count > m:
                    return False
        return True
    '''
    # this is dp
    def splitArray(self, nums, m):
        mindp = max(nums)
        maxdp = sum(nums)
        dp = [0 for i in range(mindp, maxdp+1)]
        for i in range(len(dp)):
            dp[i] = self.split_number(nums, mindp+i)
        print dp
        for i in range(len(dp)):
            if dp[i] == m:
                return mindp+i
        return -1
            
    def split_number(self, nums, upperbound):
        count = 0
        sum_cur = 0
        for num in nums:
            sum_cur += num
            if sum_cur > upperbound:
                sum_cur = num
                count += 1
        return count+1
     ''' 