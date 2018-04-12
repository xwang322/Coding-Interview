# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
import numpy
class Solution(object):
    def maxPoints(self, points):
        if len(points) < 3:
            return len(points)
        answer = 0
        for i in range(len(points)):
            slope = collections.defaultdict()
            slope['inf'] = 0
            slope[0] = 0
            same = 1
            for j in range(len(points)):
                if i == j:
                    continue
                elif points[i].x == points[j].x and points[i].y != points[j].y:
                    slope['inf'] += 1
                elif points[i].y == points[j].y and points[i].x != points[j].x:
                    slope[0] += 1
                elif points[i].y == points[j].y and points[i].x == points[j].x:
                    same += 1
                else:
                    temp = numpy.float128(points[j].y-points[i].y)/(points[j].x-points[i].x)
                    print temp
                    if temp in slope:
                        slope[temp] += 1
                    else:
                        slope[temp] = 1
            answer = max(max(slope.values())+same, answer)
        return answer