/*
* 第二题是
* The matching should cover the entire input string (not partial).
* The function prototype should be:
* bool isMatch(String str, String patter)
* Some examples:
* isMatch("aa","a") → false
* isMatch("aa","aa") → true
* isMatch("aaa","aa") → false
* isMatch("aa","a{1,3}") → true
* isMatch("aaa","a{1,3}") → false
* isMatch("ab","a{1,3}b{1,3}") → true
* isMatch("abc","a{1,3}b{1,3}c") → true
* isMatch("abbc","a{1,3}b{1,2}c") → false
* isMatch("acbac","a{1,3}b{1,3}c") → false
* isMatch("abcc","a{1,3}b{1,3}cc{1,3}") → true
**/

def isMatch(s, p):
    p_list = []
    while p.find('}') != -1:
        index1 = 0
        index2 = 0
        num = 0
        index1 = p.find('{')
        temp = ''
        temp_string = list(p[:index1])
        while temp_string:
            while len(temp_string)>1:
                p_list.append(temp_string.pop(0))
            temp = temp_string[0]
            temp_string.pop()
        p = p[index1+1:]
        index1 = p.find(',')
        index2 = p.find('}')
        temp_string = list(p[index1+1:index2])
        while temp_string:
            num = num*10+int(temp_string.pop(0))
        p_list.append(temp*(num-1))
        p = p[index2+1:]
    p_list.append(p)
    p = ''.join(p_list)
    m = len(s)
    n = len(p)
    dp = [[False for i in range(m+1)] for j in range(n+1)]
    dp[0][0] = True
    p = iter(p)
    return all(char in p for char in s)

answer = isMatch('abcc','a{1,3}b{1,3}c{1,3}')
print answer
