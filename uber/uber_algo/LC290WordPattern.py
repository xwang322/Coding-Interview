class Solution(object):
    def wordPattern(self, pattern, str):
        if not pattern or not str:
            return False
        string_split = str.strip().split()
        if len(string_split) != len(pattern):
            return False
        dictionary = {}
        for i in range(len(pattern)):
            if pattern[i] not in dictionary:
                if string_split[i] in dictionary.values():
                    return False
                else:
                    dictionary[pattern[i]] = string_split[i]
            else:
                if dictionary[pattern[i]] != string_split[i]:
                    return False
        return True
