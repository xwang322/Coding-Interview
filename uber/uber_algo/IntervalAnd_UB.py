'''
题目：Given 2 sets of intervals.
Interval is defined with left and right border and discrete points, like [2, 3], [0, 0], etc.
Set of intervals is non intersected set of sorted intervals,
for example: [0, 0], [2, 2], [5, 10] is a valid set of intervals, but [0, 0], [1, 2] is not valid, because you can write it as [0, 2]. [0, 2], [1, 5] is not valid as well, since these two intervals intersect.
You need to find the AND operation of these two sets. For example:
1st set: [0, 2], [5, 10], [16, 20]
2nd set: [1, 5], [10, 18], [20, 23]
AND Result: [1, 2], [5, 5], [10, 10], [16, 18], [20, 20]
'''
def IntervalAnd(interval1, interval2):
    if not interval1 or not interval2:
        return interval1 + interval2
    answer = []
    interval1 = sorted(interval1, key=lambda x:x[0])
    interval2 = sorted(interval2, key=lambda x:x[0])
    i = 0
    j = 0
    while i < len(interval1) and j < len(interval2):
        if interval1[i][0] > interval2[j][1] or interval2[j][0] > interval1[i][1]:
            if interval1[i][0] > interval2[j][1]:
                j += 1
            else:
                i += 1
        else:
            answer.append((max(interval1[i][0], interval2[j][0]), min(interval1[i][1], interval2[j][1])))
            if interval1[i][1] >= interval2[j][1]:
                j += 1
                interval1[i] = (answer[-1][1], interval1[i][1])
            else:
                i += 1
                interval2[j] = (answer[-1][1], interval2[j][1])
    final = []
    for each in answer:
        if final and final[-1][1]+1 == each[0]:
            temp = final.pop()
            final.append(temp[0], each[1])
        final.append(each)
    return final

answer = IntervalAnd([(0,2), (5,10), (16,20)], [(1, 5), (10, 18), (20, 23)])
print answer
