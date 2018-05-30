'''
给几个point的坐标（X,Y），给一个target的坐标，找出离target最近的k个点。
'''
import heapq
class Point(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

import math
def topKClosestPoints(points, target, k):
    if not points or not target:
        return []
    heap = []
    for point in points:
        distance = math.sqrt(abs(point.x - target.x)**2 + abs(point.y - target.y)**2)
        if len(heap) < k:
            heapq.heappush(heap, (-distance, point))
        else:
            node = heapq.heappop(heap)
            if node[0] > -distance:
                heapq.heappush(heap, node)
            else:
                heapq.heappush(heap, (-distance, point))
    answer = []
    while heap:
        answer.append(heapq.heappop(heap)[1])
    return answer

Point1 = Point(-2, 4)
Point2 = Point(0, -2)
Point3 = Point(-1, 0)
Point4 = Point(3, 5)
Point5 = Point(-2, -3)
Point6 = Point(3, 2)
target = Point(0, 0)
points = [Point1, Point2, Point3, Point4, Point5, Point6]
answer = topKClosestPoints(points, target, 2)
print answer[0].x, answer[0].y, answer[1].x, answer[1].y

# quick sort is also important as well
import collections
import math
class Point(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

def topKClosestPoints(points, target, k):
    if not points or not target:
        return []
    dictionary = collections.defaultdict(list)
    for point in points:
        distance = math.sqrt(abs(point.x - target.x)**2 + abs(point.y - target.y)**2)
        dictionary[distance].append(point)
    distances = dictionary.keys()
    quickSort(distances, 0, len(distances)-1)
    answer = []
    for i in range(k):
        answer += dictionary[distances[i]]
    return answer[:k]

def quickSort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quickSort(array, low, pivot-1)
        quickSort(array, pivot+1, low)

def partition(array, low, high):
    start = low-1
    pivot = array[high]
    for i in range(low, high):
        if array[i] <= pivot:
            start += 1
            array[start], array[i] = array[i], array[start]
    start += 1
    array[start], array[high] = array[high], array[start]
    return start

Point1 = Point(-2, 4)
Point2 = Point(0, -2)
Point3 = Point(-1, 0)
Point4 = Point(3, 5)
Point5 = Point(-2, -3)
Point6 = Point(3, 2)
target = Point(0, 0)
points = [Point1, Point2, Point3, Point4, Point5, Point6]
answer = topKClosestPoints(points, target, 2)
print answer[0].x, answer[0].y, answer[1].x, answer[1].y
