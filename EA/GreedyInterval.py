'''
给一个总的time interval，比如[1, 100]，再给一些tasks的time interval，比如[1, 50], [51, 100], [1, 99]，每次只能连续执行一个task，然后问最多能在给定的总的time interval里执行多少个task，
刚才那个例子就是最多只能执行两个[1, 50]跟[51, 100]。follow up: 如何优化时间复杂度，避免重复计算。
解法：一开始想了个DFS的解法，每次加一个interval以后再找start time比这个interval的end time要大的time interval，然后一直搜下去。
follow up的话，没有特别好的办法感觉，给了一个dp解法，先对所有的task按start time排序，然后遍历所有task，dp[task.end] = dp[0..(task.start - 1)] + 1，记录其中最大值，国人大哥觉得make sense。
但是如果时间是float的或者interval跨度很大就不能这么做了，不知道有没有更好的解法。
'''
class Interval(object):
    def __init__(self, s = 0, e = 0):
        self.start = s
        self.end = e

def mostIntervals(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key = lambda x : x.end)
    answer = []
    for interval in intervals:
        if not answer or answer[-1].end+1 <= interval.start:
            answer.append(interval)
    return len(answer)

i1 = Interval(1, 50)
i2 = Interval(51, 100)
i3 = Interval(1, 99)
intervals = [i1, i2, i3]
answer = greedyMostIntervals(intervals)
print answer
