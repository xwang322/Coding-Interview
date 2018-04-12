class Solution(object):
    def trap(self, height):
        leftmost = [0 for i in range(len(height))]
        rightmost = [0 for i in range(len(height))]
        leftmax = 0
        for i in range(len(height)):
            if height[i] > leftmax:
                leftmax = height[i]
            leftmost[i] = leftmax
        rightmax = 0
        for i in range(len(height)-1, -1, -1):
            if height[i] > rightmax:
                rightmax = height[i]
            rightmost[i] = rightmax
        sumtotal = 0
        for i in range(len(height)):
            if min(leftmost[i], rightmost[i]) > height[i]:
                sumtotal += min(leftmost[i], rightmost[i]) - height[i]
        return sumtotal
                