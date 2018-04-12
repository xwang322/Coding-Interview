/*
* Given a set of inclusive intervals
* Calculate the minimum size of a set of number
* where each interval contains at least two numbers in this set.
* Example
* given [1,3], [1,4], [2,5].
* return 2. ([2,3])
* given [2,4], [3,6], [0,2], [4,7].
* return 4. ([0,2,4,6] or [1,2,4,5])
* */
def intersectionSizeTwo(self, intervals):
    intervals = sorted(intervals, key=lambda x: x[1])
    answer = []
    for interval in intervals:
        if not answer or answer[-1] < interval[0]:
            answer.append(interval[1]-1)
            answer.append(interval[1])
        elif answer[-2] < interval[0]:
            if answer[-1] == interval[1]:
                answer.append(interval[1]-1)
            else:
                answer.append(interval[1])
    return len(answer)
