'''
然后问怎么反转一个字符串，又问怎么不用loop实现。我没反应过来他意思是要递归做法，提示了一下才知道，还被抓到了bug，搞了老半天
'''
def reverseString(s):
    # iteration
    return ''.join(list(s)[::-1])

def reverseString(s):
    # revcursion
    if not s:
        return ''
    return s[-1] + reverseString(s[:-1])

answer = reverseString('eresdds')
print answer
