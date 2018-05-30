class Solution(object):
    def judgeSquareSum(self, c):
        if c < 0:
            return False
        if c == 0:
            return True
        candidates = []
        i = 1
        while i**2 <= c:
            candidates.append(i**2)
            i += 1
        candidates.sort()
        if c in candidates:
            return True
        i = 0
        j = len(candidates)-1
        while i <= j:
            if candidates[i] + candidates[j] == c:
                return True
            elif candidates[i] + candidates[j] > c:
                j -= 1
            else:
                i += 1
        return False
