# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals
        answer = []
        start = newInterval.start
        end = newInterval.end
        i = 0
        while i <= len(intervals)-1:
            if intervals[i].end >= start:
                if end < intervals[i].start:
                    break
                start = min(intervals[i].start, start)
                end = max(intervals[i].end, end)
            else:
                answer.append(intervals[i])
            i += 1
        answer.append(Interval(start, end))
        answer += intervals[i:]
        return answer
        
