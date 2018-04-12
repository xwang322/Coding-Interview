/*
* list all the permutation of needle and haystack thing…...
**/
def permuteUnique(string):
    if not string:
        return ''
    return permute(''.join(sorted(string)))

def permute(string):
    if len(string) == 1:
        return string
    answer = []
    for index, char in enumerate(string):
        if index >0 and string[index-1] == char:
            continue
        answer += [char + p for p in permute(string[:index]+string[index+1:])]
    return answer

def strStr(needle, haystack):
    if not needle or not haystack:
        return []
    lenn = len(needle)
    lenh = len(haystack)
    if lenh < lenn:
        return []
    answer = []
    unique = permuteUnique(needle)
    for each in unique:
        for i in range(lenh-lenn+1):
            j = 0
            while j < lenn:
                if haystack[i+j] != needle[j]:
                    break
                j += 1
            if j == lenn:
                answer.append(each)
    return answer

answer = strStr('aba','abaaabaca')
print answer
