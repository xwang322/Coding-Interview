'''
从一个string当中去掉某一个字符remove(ch)
'''
def RemoveCharFromString(string, char):
    if not string:
        return ''
    if not char:
        return string
    positions = [index for index, letter in enumerate(string) if letter == char]
    if not positions:
        return string
    length = len(string)
    answer = []
    for i in range(length):
        if i not in positions:
            answer.append(string[i])
    return ''.join(answer)

answer = RemoveCharFromString('abcdaefgha','a')
print answer
