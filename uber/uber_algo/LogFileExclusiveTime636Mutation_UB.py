/*
* Phone: （直接复制粘贴过来，大家看吧)
* Compute Exclusive Time
* Given a Log File as Below:
* Function Action Timestamp
* F1 Enter 10:00:00
* F2 Enter 10:00:06
* F2 Exit 10:00:07
* F3 Enter 10:00:08
* F3 Exit 10:00:12
* F1 Exit 10:00:15
* You need to compute the exclusive time spent in a given function.
* For example:
* Exclusive time F1 = 10 second
* Exclusive time F2 = 1 second
* Exclusive time F3 = 4 second
* 这个函数调用需要考虑到递归，或者更复杂的函数调用（比如F1 call F2, F2 call F2 又 call F3, F3 又 call F2和F1等）
**/
# this one is a little different from LC 636, based on the guy posted this, depends on current situation
import time
import datetime
def LogExclusiveTime(n, logfile):
    answer = [0] * n
    stack = []
    temp = 0
    for log in logfile:
        items = log.split()
        fn, typ, timesecond = int(items[0][1:])-1, items[1], int(time.mktime(datetime.datetime.strptime(items[2], '%H:%M:%S').timetuple()))
        if not stack:
            stack.append(fn)
            temp = timesecond
        elif typ == 'Enter' and stack:
            answer[stack[-1]] += timesecond-temp
            temp = timesecond
            stack.append(fn)
        elif typ == 'Exit':
            answer[stack.pop()] += timesecond-temp
            temp = timesecond
    return answer

answer = LogExclusiveTime(3, ['F1 Enter 10:00:00','F2 Enter 10:00:06','F2 Exit 10:00:07','F3 Enter 10:00:08','F3 Exit 10:00:12','F1 Exit 10:00:15'])
print answer
