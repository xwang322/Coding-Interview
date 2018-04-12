/*
* 然后HR小哥，为人很nice帮我安排了加面，加面烙印问了开会interval问题，要求返回不开会时间，
* 他给的example还是错的，我写完了也全写出来了run cases没问题。。
**/

def RestTime(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x:x[0])
    temp = []
    answer = []
    for interval in intervals:
        if not temp:
            answer.append([0, interval[0]-1])
            temp.append(interval)
        elif temp and temp[-1][1]+1 < interval[0]:
            answer.append([temp[-1][1]+1, interval[0]-1])
            temp.append(interval)
        else:
            if temp[-1][1]+1 >= interval[1]:
                pass
            else:
                element = temp.pop()
                temp.append([element[0], interval[1]])
    final = []
    for each in answer:
        if each[0] == each[1]:
            final.append([each[0]])
        elif each[1] > each[0]:
            final.append(each)
    return final

answer = RestTime([[5, 6],[11,14],[7, 20]])
print answer
