# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        if not intervals:
            return True
        intervals = sorted(intervals, key=lambda x:x.start)
        i = 0
        while i < len(intervals):
            if i < len(intervals)-1:
                if intervals[i].end > intervals[i+1].start:
                    return False
            i +=1
        return True
