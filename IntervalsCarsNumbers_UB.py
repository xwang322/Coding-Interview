'''
给一堆users，和她们的上下车的时间，然后给出所有的乘车数目变化的时间点，扩展是有可能同一个user id，应该不同的人打开了app，乘车. 所以时间有overlap，如何handle
'''
# As to same user id different persons, same codes, just put them into a large array and process.....
import collections
def IntervalTimeAndNumber(users):
    if not users:
        return []
    temp = []
    for user in users:
        for trip in user:
            temp.append(trip)
    temp = sorted(temp, key=lambda x:x[0])
    tmp = collections.deque()
    answer = []
    count = 0
    for trip in temp:
        if not tmp:
            tmp.append(trip)
            count += 1
            answer.append((trip[0], 0))
        elif trip[0] >= tmp[0][1]:
            while tmp:
                if trip[0] >= tmp[0][1]:
                    element = tmp.popleft()
                    answer.append((element[1], count))
                    count -= 1
                else:
                    break
            tmp.append(trip)
            answer.append((trip[0], count))
            count += 1
        else:
            tmp.append(trip)
            answer.append((trip[0], count))
            count += 1
    tmp = sorted(tmp, key=lambda x:x[1])
    while tmp:
        answer.append((tmp[0][1], count))
        tmp.pop(0)
        count -= 1
    final = []
    for timestamp in answer:
        if not final:
            final.append(timestamp)
        elif timestamp[1] == final[-1][1]:
            element = final.pop()
            newelement = (timestamp[0], element[1])
            final.append(newelement)
        elif timestamp[0] == final[-1][0]:
            pass
        else:
            final.append(timestamp)
    return final

answer = IntervalTimeAndNumber([[[1,2], [5,7], [8,12], [19,24]],[[3,6],[7,8],[13,17],[20,23]]])
print answer
