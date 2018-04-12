# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        # sort by first element
        if not intervals:
            return 0
        intervals = sorted(intervals, key = lambda x:x.start)
        end = -float('inf')
        count = 0
        for interval in intervals:
            if interval.start < end:
                end = min(end, interval.end)
                count += 1
            else:
                end = interval.end
        return count
        
        