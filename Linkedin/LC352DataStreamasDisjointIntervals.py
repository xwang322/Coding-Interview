# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        self.list = []

    def addNum(self, val):
        left = 0
        right = len(self.list)-1
        while left <= right:
            mid = (left+right)/2
            interval = self.list[mid]
            if interval.start <= val <= interval.end:
                return
            elif interval.start > val:
                right = mid-1
            else:
                left = mid+1
        pos = min(left, right)+1
        self.list.insert(pos, Interval(val, val))
        if pos+1 < len(self.list) and val == self.list[pos+1].start-1:
            self.list[pos].end = self.list[pos+1].end
            self.list[pos+1:pos+2] = []
        if pos-1 >= 0 and val == self.list[pos-1].end+1:
            self.list[pos-1].end = self.list[pos].end
            self.list[pos:pos+1] = []


    def getIntervals(self):
        return self.list

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
