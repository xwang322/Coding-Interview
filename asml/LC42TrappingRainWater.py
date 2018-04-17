class Solution(object):
    def trap(self, height):
        if not height:
            return 0
        left = [0 for i in range(len(height))]
        right = [0 for i in range(len(height))]
        leftmost = 0
        for i in range(len(height)):
            if height[i] > leftmost:
                leftmost = height[i]
            left[i] = leftmost
        rightmost = 0
        for i in range(len(height)-1, -1, -1):
            if height[i] > rightmost:
                rightmost = height[i]
            right[i] = rightmost
        answer = 0
        for i in range(len(height)):
            if min(left[i], right[i]) > height[i]:
                answer += (min(left[i], right[i])-height[i])
        return answer
        
