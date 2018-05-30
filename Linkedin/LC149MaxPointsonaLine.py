# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

# directly use float calculation induces some errors, when working on this solution, needs to take care of the dictionary is empty case. So use a tempmax to avoid that, gcd is important.
class Solution(object):
    def maxPoints(self, points):
        if not points:
            return 0
        if len(points) <= 2:
            return len(points)
        answer = 0
        for i in range(len(points)-1):
            same = 0
            dictionary = {}
            tempmax = 0
            for j in range(i+1, len(points)):
                x1 = points[i].x
                x2 = points[j].x
                y1 = points[i].y
                y2 = points[j].y
                dx = x2 - x1
                dy = y2 - y1
                if dx == 0 and dy == 0:
                    same += 1
                    continue
                slope = self.gcd(dy, dx)
                dy //= slope
                dx //= slope
                dictionary[(dx, dy)] = dictionary.get((dx, dy), 0) + 1
                tempmax = max(tempmax, dictionary[(dx, dy)])
            answer = max(answer, tempmax+same+1)
        return answer

    def gcd(self, a, b):
        if not b:
            return a
        else:
            return self.gcd(b, a%b)
