/*
* 然后又出了一个需要几件会议室的那个题，都是原题。楼主小心翼翼管好嘴，没有说错话。。。
* 结果还是挂了，因为烙印说看了，，第一轮的feedback，，，决定挂了我。。。。
**/

import heapq
def HowManyRooms(intervals):
    if not intervals:
        return 0
    heap = []
    for interval in intervals:
        if heap and heap[0] <= interval[0]:
            heapq.heapreplace(heap, interval[1])
        else:
            heapq.heappush(heap, interval[1])
    return len(heap)

answer = HowManyRooms([[0, 30],[5, 10],[15, 20]])
print answer
