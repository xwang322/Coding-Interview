class Solution(object):
    def wordPatternMatch(self, pattern, string):
        return self.dfs(pattern, string, {})

    def dfs(self, pattern, string, dictionary):
        if pattern in dictionary and dictionary[pattern] == string:
            return True
        if not pattern and not string:
            return True
        if (pattern and not string) or (string and not pattern):
            return False
        for i in range(1, len(string)-len(pattern)+2):
            if pattern[0] not in dictionary and string[:i] not in dictionary.values():
                dictionary[pattern[0]] = string[:i]
                if self.dfs(pattern[1:], string[i:], dictionary):
                    return True
                else:
                    del dictionary[pattern[0]]
            elif pattern[0] in dictionary and string[:i] in dictionary.values():
                if dictionary[pattern[0]] != string[:i]:
                    return False
                elif self.dfs(pattern[1:], string[i:], dictionary):
                    return True
        return False
