/*
* add number in string format，刚开始给的base是2，然后followup给任意base，我写了个base 《＝10 的，
* 然后问如果是hex怎么办，就说了思路，没写代码，挺简单的也是秒了。
**/
# for base  <= 10 cases
def addNumberStringFormat(str1, str2, base):
    if not str1:
        return str2
    if not str2:
        return str1
    print convert(str1, base), convert(str2, base)
    return str(convert(str1, base)+convert(str2, base))

def convert(string, base):
    answer = 0
    i = 0
    sign = 1
    while i < len(string):
        if string[i].isdigit() >= base or not string[i].isdigit():
            return 0
        elif i == 0 and string[i] == '-' and string[1:].isdigit():
            sign = -1
        answer = answer*base + ord(string[i]) - ord('0')
        i += 1
    return answer*sign

answer = addNumberStringFormat('1011','1101', 8)
print answer

# for hex cases, we need to extend that a little bit
def addNumberStringFormatHex(str1, str2, base):
    if not str1:
        return str2
    if not str2:
        return str1
    print convert(str1, base), convert(str2, base)
    return str(convert(str1, base)+convert(str2, base))

def convert(string, base):
    answer = 0
    i = 0
    sign = 1
    dictionary
    while i < len(string):
        if string[i].isdigit() >= base or not string[i].isdigit():
            return 0
        elif i == 0 and string[i] == '-' and string[1:].isdigit():
            sign = -1
        answer = answer*base + ord(string[i]) - ord('0')
        i += 1
    return answer*sign

answer = addNumberStringFormat('1011','1101', 8)
print answer
