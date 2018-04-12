# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        answer = []
        intervals = sorted(intervals, key=lambda x:x.start)
        for interval in intervals:
            if answer and answer[-1].end >= interval.start:
                if answer[-1].end <= interval.end:
                    answer[-1].end = interval.end
            else:
                answer.append(interval)
        return answer
        
