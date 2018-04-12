# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        if not intervals:
            return True
        answer = []
        intervals = sorted(intervals, key=lambda x: x.start)
        for interval in intervals:
            if not answer:
                answer.append(interval)
            elif answer[-1].end > interval.start:
                return False
            else:
                answer.append(interval)
        return True
