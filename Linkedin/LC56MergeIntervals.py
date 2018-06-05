# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x:x.start)
        answer = []
        for interval in intervals:
            if not answer or answer[-1].end < interval.start:
                answer.append(interval)
            else:
                answer[-1].end = max(answer[-1].end, interval.end)
        return answer