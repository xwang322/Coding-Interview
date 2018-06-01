'''
吴氏七，这题稍微有点变形，要设计一个class，支持addInterval()和getWeightedSum()
'''
 Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def addInterval(self, intervals, newInterval):
        if not newInterval:
            return intervals
        if not intervals:
            return [newInterval]
        answer = []
        start = newInterval.start
        end = newInterval.end
        i = 0
        while i < len(intervals):
            if intervals[i].end >= start:
                if end < intervals[i].start:
                    break
                start = min(start, intervals[i].start)
                end = max(end, intervals[i].end)
            else:
                answer.append(intervals[i])
            i += 1
        answer.append(Interval(start, end))
        while i < len(intervals):
            answer.append(intervals[i])
            i += 1
        return answer

    def getWeightedSum(self, intervals, newInterval):
        # I think getWeightedSum means get the total coverage
        if not newInterval or not newInterval:
            return 0
        start = newInterval.start
        end = newInterval.end
        i = 0
        overlap = 0
        while i < len(intervals):
            if intervals[i].end >= start:
                overlap += 1
                if end < intervals[i].start:
                    overlap -= 1
                    break
                start = min(start, intervals[i].start)
                end = max(end, intervals[i].end)
            i += 1
        return overlap
