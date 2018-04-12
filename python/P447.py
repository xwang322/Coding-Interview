class Solution(object):
    def numberOfBoomerangs(self, points):
        answer = 0
        for point in points:
            temp = {}
            for p in points:
                a = point[0] - p[0]
                b = point[1] - p[1]
                temp[a*a+b*b] = 1+temp.get(a*a+b*b, 0)
            for key in temp:
                answer += temp[key]*(temp[key]-1)
        return answer
        