class Solution(object):
    """
    def isSubsequence(self, s, t):
        queue = collections.deque(s) #de means double-ended in Python
        for c in t:
            if not queue:
                return True
            if c == queue[0]:
                queue.popleft()
        return not queue
    """
    def isSubsequence(self, s, t):
        t = iter(t)
        return all(c in t for c in s)
    # follow-up questions use binary search
