class Solution(object):
    def isIsomorphic(self, s, t):
        dictionary = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in dictionary and t[i] not in dictionary.values():
                dictionary[s[i]] = t[i]
            elif s[i] not in dictionary and t[i] in dictionary.values():
                return False
            elif dictionary[s[i]] != t[i]:
                return False
        return True
        
