# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        heap = []
        intervals = sorted(intervals, key=lambda x:x.start)
        for interval in intervals:
            if not heap:
                heapq.heappush(heap, interval.end)
            else:
                first = heapq.heappop(heap)
                if first > interval.start:
                    heapq.heappush(heap, interval.end)
                    heapq.heappush(heap, first)
                else:
                    heapq.heappush(heap, interval.end)
        return len(heap)
                
