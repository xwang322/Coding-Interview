/*
* 给一堆interval，比如{3,6},{2,4}，然后给一个数，返回哪些interval包含了这个数，比如5就返回{3,6},{2,4}，2就只返回{2,4}
**/

def IntervalsContains(intervals, number):
    if not intervals:
        return []
    answer = []
    intervals = sorted(intervals, key=lambda x:x[0])
    for interval in intervals:
        if interval[0]<= number<= interval[1]:
            answer.append(interval)
        elif interval[0] > number:
            break
        elif interval[1] < number:
            continue
    return answer

answer = IntervalsContains([(3,7), (2,9), (1,6)], 6)
print answer
