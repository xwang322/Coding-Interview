/*
* 本来说是澳洲人，结果现场变成了一个口音一般重的烙胤给一串电话号码和一串单词表，找匹配word最多的电话号码
*写的磕磕巴巴，还出了compile error。。。
# I do not think this needs Trie but anyway....
*电面：之前帖子里有人提到过，就是找能匹配到最多words的电话号码，用trie tree建word dict，然后每个电话号码用bfs扫满足条件的branch就好了。
**/
# map digits to string direction
import collections
def letterAndnumbers(string_list, digits_list):
    if not string_list or not digits_list:
        return []
    dictionary1 = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    dictionary2 = {'a':'2', 'b':'2', 'c':'2', 'd':'3', 'e':'3', 'f':'3', 'g':'4', 'h':'4', 'i':'4', 'j':'5', 'k':'5', 'l':'5', 'm':'6', 'n':'6','o':'6','p':'7', 'q':'7', 'r':'7', 's':'7', 't':'8', 'u':'8', 'v':'8', 'w':'9', 'x':'9', 'y':'9', 'z':'9'}
    answer = ''
    string_counter = []
    length = len(string_list[0])
    for string in string_list:
        dfs(dictionary2, string, string_counter, '', length)
    string_list_counter = collections.Counter(string_counter)
    for key, value in sorted(string_list_counter.iteritems(),key=lambda (k,v):(v,k)):
        if key in digits_list:
            answer = key
    return answer

def dfs(dictionary, string, string_counter, path, length):
    if not string and len(path) == length:
        string_counter.append(path)
        return
    for index, char in enumerate(list(string)):
        dfs(dictionary, string[index+1:], string_counter, path+dictionary[char], length)

answer = letterAndnumbers(['adh','abg','adg'], ['234'])
print answer

# map string to digits direction
import collections
def letterAndnumbers(string_list, digits_list):
    if not string_list or not digits_list:
        return []
    dictionary1 = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    dictionary2 = {'a':'2', 'b':'2', 'c':'2', 'd':'3', 'e':'3', 'f':'3', 'g':'4', 'h':'4', 'i':'4', 'j':'5', 'k':'5', 'l':'5', 'm':'6', 'n':'6','o':'6','p':'7', 'q':'7', 'r':'7', 's':'7', 't':'8', 'u':'8', 'v':'8', 'w':'9', 'x':'9', 'y':'9', 'z':'9'}
    dictionary = {}
    length = len(digits_list[0])
    for digits in digits_list:
        digits_counter = []
        dfs(dictionary1, digits, digits_counter, '', length)
        for each in digits_counter:
            if each in string_list:
                dictionary[digits] = dictionary.get(digits, 0)+1
    return max(dictionary)


def dfs(dictionary, digits, digits_counter, path, length):
    if not digits and len(path) == length:
        digits_counter.append(path)
        return
    for index, char in enumerate(list(digits)):
        for each in dictionary[char]:
            dfs(dictionary, digits[index+1:], digits_counter, path+each, length)

answer = letterAndnumbers(['adh','abg','adg'], ['234', '224'])
print answer
