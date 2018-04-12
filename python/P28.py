class Solution(object):
    def strStr(self, haystack, needle):
        if not haystack and not needle:
            return 0
        if len(needle) > len(haystack):
            return -1
        len_h = len(haystack)
        len_n = len(needle)
        for i in range(len_h-len_n+1):
            if haystack[i:i+len_n] == needle:
                return i
        return -1
        