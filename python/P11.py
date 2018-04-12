class Solution(object):
    def maxArea(self, height):
        left = 0; right = len(height)-1
        answer = 0
        while left < right:
            temp = min(height[left], height[right]) * (right-left)
            if temp > answer:
                answer = temp
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return answer
        