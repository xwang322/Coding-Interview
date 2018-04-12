class Solution(object):
    def findMinArrowShots(self, points):
        '''
        # by ending position
        points = sorted(points, key = lambda x:x[1])
        answer = 0
        pivot = -float('inf')
        for point in points:
            if point[0] > pivot:
                pivot = point[1]
                answer += 1
        return answer
        '''
        # by starting position
        points = sorted(points, key = lambda x:x[0])
        answer = 0
        pivot = -float('inf')
        for point in points:
            if point[0] > pivot:
                answer += 1
                pivot = point[1]
            elif point[1] < pivot:
                pivot = point[1]
        return answer