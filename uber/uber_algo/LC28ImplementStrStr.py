class Solution(object):
    def strStr(self, haystack, needle):
        if not haystack and not needle:
            return 0
        elif haystack and not needle:
            return 0
        elif not haystack and needle:
            return -1
        elif len(haystack) < len(needle):
            return -1
        else:
            for i in range(len(haystack)-len(needle)+1):
                j = 0
                while j < len(needle):
                    if haystack[i+j] == needle[j]:
                        j += 1
                    else:
                        break
                if j == len(needle):
                    return i
            return -1
                    
