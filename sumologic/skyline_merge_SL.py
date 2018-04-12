/*
* skyline变形 merge interval + follow up skyline  List of intervals: [1,3], [4,10], [20,30].
* check if given interval like [5,10] are occupied by the intervals.
* Finding the area of overlapping boxes (several variants)
* Given a set of overlapping rectangles with same base and height, find the area covered by these rectangles.
**/
def merge(self, intervals):
    answer = []
    for i in sorted(intervals, key=lambda i:i.start):
        if answer and answer[-1].end >= i.start:
            answer[-1].end = max(i.end, answer[-1].end)
        else:
            answer.append(i)
    return answer
