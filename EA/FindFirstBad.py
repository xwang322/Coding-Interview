'''
第一题：一个boolean array，里面是good bad的flag，如果bad发生，他之后就都是bad. 比如good, good, bad, bad,....., bad。求第一个bad。很简单，binary search.
'''
import bisect
def findFirstBad(flags):
    if not flags or -1 not in flags:
        return -1
    new_flag = []
    for flag in flags:
        if flag == 1:
            new_flag.append(-1)
        else:
            new_flag.append(1)
    return bisect.bisect_left(new_flag, 1)

answer = findFirstBad([1, 1, 1, -1, -1, -1])
print answer
