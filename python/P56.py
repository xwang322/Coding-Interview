# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        answer = []
        for i in sorted(intervals, key=lambda i:i.start):
            if answer and answer[-1].end >= i.start:
                answer[-1].end = max(i.end, answer[-1].end)
            else:
                answer.append(i)
        return answer