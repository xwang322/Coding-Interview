class Solution(object):
    def constructRectangle(self, area):
        square = int(math.sqrt(area))
        L, W = area, 1
        for x in range(square, 0, -1):
            if area%x == 0:
                L, W = area/x, x
                break
        return [L, W]
        