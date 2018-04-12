class Solution(object):
    def trap(self, height):
        if not height:
            return 0
        if len(height) == 1:
            return 0
        start = 0
        end = 0
        answer = 0
        visited = [False for i in range(len(height))]
        while end <= len(height)-1:
            while start <= len(height)-1 and height[start] == 0:
                start += 1
            end = start+1
            while end <= len(height)-1 and height[start] > height[end]:
                end += 1
            if end != len(height):
                for i in range(start+1, end):
                    answer += height[start]-height[i] 
                visited[start] = True
                start = end
        start1 = len(height)-1
        end1 = len(height)-1
        answer1 = 0
        while end1 >= 0:
            while start1 >= 0 and height[start1] == 0:
                start1 -= 1
            end1 = start1-1
            while end1 >= 0 and height[start1] > height[end1]:
                end1 -= 1
            if end1 != -1 and not visited[end1]:
                for i in range(start1-1, end1, -1):
                    answer1 += height[start1]-height[i] 
            start1 = end1
        return answer+answer1