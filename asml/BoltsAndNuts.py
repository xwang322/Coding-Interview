/*
* 难题： 2个array，一个里面都是各种不同形状的螺丝钉，一个都是各种不同形状的螺母，无需排列，如何让他们一一对应。 nlogn的问题
**/
import heapq
def BoltsAndNuts(bolts, nuts):
    if not bolts or not nuts:
        return []
    answer = []
    heap1 = []
    heap2 = []
    for index, bolt in enumerate(bolts):
        heapq.heappush(heap1, (bolt, index))
    for index, nut in enumerate(nuts):
        heapq.heappush(heap2, (nut, index))
    while heap1 and heap2:
        bolt, index1 = heapq.heappop(heap1)
        nut, index2 = heapq.heappop(heap2)
        if bolt == nut:
            answer.append((index1, index2))
        elif bolt > nut:
            heapq.heappush(heap1, (bolt, index1))
        else:
            heapq.heappush(heap2, (nut, index2))
    return answer

answer = BoltsAndNuts([3,5,6,8,12,14],[3,1,5,8,9,12])
print answer
