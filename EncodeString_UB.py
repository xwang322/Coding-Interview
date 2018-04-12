/*
* 面试之前又刷了一遍uber的tag，还来地里看了不少面经，结果竟然遇到一个新题（其实leetcode有类似的可能真的是自己没做到）～
* 面试官是国人，感觉工作了很多年特别有经验的那种，题目就是encode decode string （只有数字和小写字母）, 让你自己设计encode的方法，得到的string要不能比原来长就可以了。。
* 我最开始以为是encode/decode tiny url那种，想用hashmap，面试官说不能用hash，你不能把map一起传给decoder，然后我就设计了一个特别简单直接的。。
* abbcd1123变成a2bcd2BCD
* 就是把数字全部变成大写字符（'A' - 'J'），然后出现次数大于2次的在前面加一下出现的次数。
* 写完了之后面试官又让我decode，跟leetcode 394应该差不多。我没用stack直接做的。。因为数字都被转换成了大写字母，所以所有的数字只表示出现的次数，正常扫一遍就行。。。
* decode跑出来稍微有点小问题，然后时间就到了（感觉面试官特别赶时间）。。
* 就做了这一道题，不知道是不是还应该有第二题。。。。感觉大概率要跪了。。。最后跟面试官说了新年快乐，希望能放我一马给个offer啊
**/
def encodeString(string):
    if not string:
        return string
    dictionary = {'0':'A', '1':'B', '2':'C', '3':'D', '4':'E', '5':'F', '6':'G', '7':'H', '8':'I', '9':'J'}
    temp = []
    start = 0
    answer = []
    for i in range(len(string)):
        if string[i] in dictionary:
            temp.append(dictionary[string[i]])
        else:
            temp.append(string[i])
    temp_string = ''.join(temp)
    for i in range(len(temp_string)-1):
        if temp_string[i] == temp_string[i+1]:
            continue
        else:
            if i-start+1 > 1:
                answer.append(str(i-start+1)+temp_string[i])
            else:
                answer.append(temp_string[i])
            start = i+1
    if start == len(temp_string)-1:
        answer.append(temp_string[-1])
    else:
        answer.append(str(len(temp_string)-start)+temp_string[-1])
    return ''.join(answer)

def decodeString(string):
    if not string:
        return string
    dictionary_decode = {'A':'0', 'B':'1', 'C':'2', 'D':'3', 'E':'4', 'F':'5', 'G':'6', 'H':'7', 'I':'8', 'J':'9'}
    temp_answer = []
    temp = 0
    for i in range(len(string)):
        if 0 <= ord(string[i])-ord('0') <= 9:
            temp = temp*10 + int(string[i])
        else:
            if temp:
                temp_answer.append(temp*string[i])
                temp = 0
            else:
                temp_answer.append(string[i])
    answer = []
    temp_answer = ''.join(temp_answer)
    for i in range(len(temp_answer)):
        if temp_answer[i] in dictionary_decode:
            answer.append(dictionary_decode[temp_answer[i]])
        else:
            answer.append(temp_answer[i])
    return ''.join(answer)

answer = decodeString(encodeString('bb6bacac001ccccccccccccc'))
print answer

/*
* 压缩字符串，要求一定要比原来短。输入字符串只包含数字和小写字母
* 比如 “aaabbbb”, 可以压缩为"CaDb"
**/
def encodeString(string):
    if not string:
        return string
    temp = []
    start = 0
    answer = []
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            continue
        else:
            if i-start+1 > 1:
                answer.append(chr(i-start+ord('A'))+string[i])
            else:
                answer.append(string[i])
            start = i+1
    if start == len(string)-1:
        answer.append(string[-1])
    else:
        answer.append(chr(len(string)-1-start+ord('A'))+string[-1])
    return ''.join(answer)

def decodeString(string):
    if not string:
        return string
    answer = []
    temp = 0
    for i in range(len(string)):
        if 1 <= ord(string[i])-ord('A') <= 25:
            temp = ord(string[i])-ord('A')+1
        else:
            if temp:
                answer.append(temp*string[i])
                temp = 0
            else:
                answer.append(string[i])
    return ''.join(answer)

answer = decodeString(encodeString('bb6bacac001ccccccccccccc'))
print answer
