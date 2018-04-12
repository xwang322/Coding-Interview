# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x: x.start)
        answer = []
        for interval in intervals:
            if answer and answer[-1][1] >= interval.start:
                answer[-1] = [answer[-1][0], max(interval.end, answer[-1][1])]
            else:
                answer.append([interval.start, interval.end])
        return answer
                