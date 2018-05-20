'''
删除字符串中的指定字符
'''
def RemoveCharFromString(string, char):
    if not string or not char:
        return string
    answer = ''
    for each in string:
        if each != char:
            answer += each
    return answer

answer = RemoveCharFromString('abcdaefgha','a')
print answer
