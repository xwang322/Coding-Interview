# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        candidate1 = 0
        candidate2 = n-1
        for i in range(1, n):
            if knows(candidate1, i):
                candidate1 = i
        for i in range(n-2, -1, -1):
            if knows(candidate2, i):
                candidate2 = i
        if candidate1 != candidate2:
            return -1
        return candidate1
        
