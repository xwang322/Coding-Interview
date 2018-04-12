/*
* 第一题： 给我一个string of words， space seperated， 要求我把里面所有出现的数字 全部变成 *****
* follow up： 如果不是space seperated，里面有各种特殊符号怎么办
**/
def ConvertNumberToStars(string):
    if not string:
        return ''
    temp = []
    string_list = string.strip().split()
    for word in string_list:
        temp_string = ''
        for char in word:
            if '0'<=char<='9':
                temp_string += '*****'
            else:
                temp_string += char
        temp.append(temp_string)
    return ' '.join(temp)

answer = ConvertNumberToStars('Thi2 is a goo4 t6me!')
print answer

def ConvertNumberToStarsFollowUp(string):
    if not string:
        return ''
    answer = ''
    string = string.strip()
    for char in string:
        if '0'<=char<='9':
            answer += '*****'
        else:
            answer += char
    return answer

answer = ConvertNumberToStarsFollowUp('Thi2is!a goo4   +t6&@me!')
print answer
