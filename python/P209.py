class Solution(object):
    def minSubArrayLen(self, s, nums):
        '''Two pointer
        if not nums:
            return 0
        sum_array = [0 for i in range(len(nums)+1)]
        for i in range(len(nums)):
            sum_array[i+1] = sum_array[i]+nums[i]
        if sum_array[-1] < s:
            return 0
        start = 0
        end = 0
        count = len(nums)+100
        while start <= end and end <= len(sum_array)-1:
            if sum_array[end]-sum_array[start] >= s:
                count = min(count, end-start)
                start += 1
            else:
                end += 1
        return count
        '''
        # Binary Search
        if not nums:
            return 0
        sum_array = [0 for i in range(len(nums)+1)]
        for i in range(len(nums)):
            sum_array[i+1] = sum_array[i]+nums[i]
        if sum_array[-1] < s:
            return 0
        answer = len(nums)+1
        left = 0
        for i in range(1, len(sum_array)):
            if sum_array[i] >= s:
                right = i
                left = self.findleft(left, right, sum_array, sum_array[i], s)
                answer = min(answer, right-left+1)
        return answer
            
    def findleft(self, left, right, sum_array, num, s):
        while left < right:
            mid = (left+right)/2
            if num-sum_array[mid] >= s:
                left = mid + 1
            else:
                right = mid
        return left
                