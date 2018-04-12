/*
* addInterval以及getCoverage
* 比如说[1, 5], [2, 8] 变成了[1, 8] coverage就是8
**/
def MergeIntervalandCoverage(intervals):
    if not intervals:
        return []
    answer = []
    coverage = []
    intervals = sorted(intervals, key=lambda x:x[0])
    for interval in intervals:
        if answer and answer[-1][1] >= interval[0]:
            if answer[-1][1] <= interval[1]:
                answer[-1][1] = interval[1]
                coverage[-1] = answer[-1][1]-answer[-1][0]+1
        else:
            answer.append(interval)
            coverage.append(answer[-1][1]-answer[-1][0]+1)
    return coverage

answer = MergeIntervalandCoverage([[1,4],[5,8],[3,7],[2,6],[5,8],[11,11]])
print answer
