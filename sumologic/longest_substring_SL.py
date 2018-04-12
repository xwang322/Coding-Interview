/*
* 一个LC 3 的变种,需要打出来最长的那个字符串.
**/
def function(s):
    count = {}
    answer, start, end = 0, 0, 0
    temp = ''
    for char in s:
        end += 1
        count[char] = count.get(char, 0) + 1
        while count[char] > 1:
            count[s[start]] -= 1
            start += 1
        if end-start > answer:
            temp = s[start:end]
        answer = max(answer, end-start)
    return temp
