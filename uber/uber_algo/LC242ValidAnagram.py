class Solution(object):
    def isAnagram(self, s, t):
        if not t:
            return True
        s_dict = collections.Counter(s)
        t_dict = collections.Counter(t)
        return s_dict == t_dict