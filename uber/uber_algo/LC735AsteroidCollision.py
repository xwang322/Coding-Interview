class Solution(object):
    def asteroidCollision(self, asteroids):
        while True:
            stack = []
            prev = len(asteroids)
            i = 0
            while i <= len(asteroids)-2:
                if (asteroids[i]<0 and asteroids[i+1]<0) or (asteroids[i]>0 and asteroids[i+1]>0) or (asteroids[i]<0<asteroids[i+1]):
                    stack.append(asteroids[i])
                    i += 1
                elif abs(asteroids[i]) > abs(asteroids[i+1]):
                    del asteroids[i+1]
                elif abs(asteroids[i]) == abs(asteroids[i+1]):   
                    del asteroids[i+1]
                    del asteroids[i]
                else:
                    i += 1  # it may not update clearly for here
            if i == len(asteroids)-1:
                stack.append(asteroids[i])
            if len(stack) == prev:
                break
            else:
                asteroids = stack
        return asteroids
                    