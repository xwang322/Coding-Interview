class Solution(object):
    def getSkyline(self, buildings):
        if not buildings or len(buildings) == 0:
            return []
        if len(buildings) == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
        mid = (len(buildings)-1)/2
        left = self.getSkyline(buildings[0:mid+1])
        right = self.getSkyline(buildings[mid+1:])
        return self.merge(left, right)
    
    def merge(self, left, right):
        h1, h2, res = 0, 0, []
        while left and right:
            if left[0][0] < right[0][0]:
                pos, h1 = left[0]
                left = left[1:]
            elif left[0][0] > right[0][0]:
                pos, h2 = right[0]
                right = right[1:]
            else:
                pos, h1 = left[0]
                h2 = right[0][1]
                left = left[1:]
                right = right[1:]
            H = max(h1, h2)
            if not res or H != res[-1][1]:
                res.append([pos, H])
        if left:
            res += left
        if right:
            res += right
        return res
                