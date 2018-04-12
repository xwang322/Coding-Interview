/*
Question: Magical Strings
规则是一个字符串只能由 a, e, i, o, u 中的字符组成，每个字符都可以用任意次，但是必须满足规则：
a后面只能跟e
e后面只能跟a或i
i后面可以跟a, e, o, u中任一
o后面只能跟i或u附件
u后面只能跟a
题目输入是一个数字n，求满足以上规则且长度为n的字符串一共有多少个，输出个数对于1000000007的模。
**/

Code:
def numofCombStr(n):
    a, e, i, o, u = 1, 1, 1, 1, 1
    j = 1
    while j <= n:
        at = e
        et = a+i
        it = a+e+o+u
        ot = i+u
        ut = a
        a,e,i,o,u = at, et, it, ot, ut
        j += 1
    return a+e+i+o+u
