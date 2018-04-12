class Solution(object):
    def thirdMax(self, nums):
        first = second = third = None
        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            elif second < num < first:
                third = second
                second = num
            elif third < num < second:
                third = num
        if third is not None:
            return third
        else:
            return first
                