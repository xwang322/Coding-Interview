# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        if len(intervals) == 0 or len(intervals) == 1:
            return [-1]
        answer = []
        inter_sorted = sorted((x.start, i) for i, x in enumerate(intervals))
        for interval in intervals:
            index = bisect.bisect_right(inter_sorted, (interval.end,))
            answer.append(inter_sorted[index][1] if index < len(intervals) else -1)
        return answer
        