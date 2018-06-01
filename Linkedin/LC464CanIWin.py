class Solution(object):
    def helper(self, allowed, target, so_far, cache):
        if len(allowed) == 0:
            return False
        state = tuple(allowed)
        if state in cache:
            return cache[state]
        else:
            cache[state] = False
            if max(allowed) + so_far >= target:
                cache[state] = True
            else:
                for x in allowed:
                    new_allowed = [y for y in allowed if x!=y]
                    if self.helper(new_allowed, target, so_far+x, cache) ==  False:
                        cache[state] = True
                        break
            return cache[state]

    def canIWin(self, maxChoosableInteger, desiredTotal):
        allowed = [x for x in range(1, maxChoosableInteger+1)]
        if sum(allowed) < desiredTotal:
            return False
        return self.helper(allowed, desiredTotal, 0, {})
