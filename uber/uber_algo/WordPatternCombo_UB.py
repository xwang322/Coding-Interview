/*
* Coding:
* 第一题： pattern match:
* 给2个string a, string b,
* a = "red red black", b = "aab" --> true
* a = "red green black", b = "abc" --> true
* a = "red red green", b = "abb" --> false
* a = "red red", b = "bb" --> true
* 第二题： 第一题的拓展：
* 如果第一题中的string a 去掉空格，变成“redredblack”, string b 不变，应该怎么做。
* 这题最后没有做完。
* 今天收到HR的拒电话， 桑心。。。。
**/


class Solution(object):
    def wordPattern(self, pattern, str):
        str_list = str.strip().split()
        if len(pattern) != len(str_list):
            return False
        dictionary = {}
        for i in range(len(pattern)):
            if pattern[i] not in dictionary.keys() and str_list[i] not in dictionary.values():
                dictionary[pattern[i]] = str_list[i]
            elif pattern[i] in dictionary.keys() and str_list[i] in dictionary.values():
                if dictionary[pattern[i]] != str_list[i]:
                    return False
            else:
                return False
        return True

class Solution(object):
    def wordPatternMatch(self, pattern, str):
        return self.dfs({}, pattern, str)

    def dfs(self, dictionary, pattern, str):
        if not str and not pattern:
            return True
        if (not str and pattern) or (not pattern and str):
            return False
        if pattern in dictionary and dictionary[pattern] == str:
            return True
        for i in range(1, len(str)-len(pattern)+2):
            if pattern[0] not in dictionary.keys() and str[:i] not in dictionary.values():
                dictionary[pattern[0]] = str[:i]
                print dictionary
                if self.dfs(dictionary, pattern[1:], str[i:]):
                    return True
                else:
                    del dictionary[pattern[0]]
            # do not write the other 2 cases where one in and the other not in because that will return False directly halfway without checking all, leave it there temporarily
            elif pattern[0] in dictionary.keys() and str[:i] in dictionary.values():
                if dictionary[pattern[0]] != str[:i]:
                    return False
                else:
                    if self.dfs(dictionary, pattern[1:], str[i:]):
                        return True
        return False
