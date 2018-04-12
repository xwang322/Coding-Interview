'''
利口205
'''
class Solution(object):
    def isIsomorphic(self, s, t):
        if not s or not t:
            return s==t
        if len(s) != len(t):
            return False
        dictionary = {}
        for i in range(len(s)):
            if s[i] not in dictionary:
                if t[i] not in dictionary.values():
                    dictionary[s[i]] = t[i]
                else:
                    return False
            else:
                if dictionary[s[i]] != t[i]:
                    return False
                else:
                    pass
        return True
