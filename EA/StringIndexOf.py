'''
实现String的indexOf(sub)
LC28
'''
def strStr(self, haystack, needle):
    if not needle:
        return 0
    elif not haystack:
        return -1
    else:
        if len(needle) > len(needle):
            return -1
        else:
            i = 0
            for i in range(len(haystack)-len(needle)+1):
                if haystack[i] == needle[0]:
                    if haystack[i:i+len(needle)] == needle:
                        return i
    return -1
