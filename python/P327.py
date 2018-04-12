class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        prefix, thissum, answer = [0], 0, 0
        for num in nums:
            thissum += num
            answer += bisect.bisect_right(prefix, thissum-lower) - bisect.bisect_left(prefix, thissum-upper)
            bisect.insort(prefix, thissum)
        return answer
        