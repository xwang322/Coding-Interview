class Solution(object):
    def isHappy(self, n):
        visited = set()
        temp = 0
        while n:
            for char in str(n):
                temp += int(char)**2
            if temp == 1:
                return True
            if temp in visited:
                return False
            visited.add(temp)
            n = temp
            temp = 0
        
