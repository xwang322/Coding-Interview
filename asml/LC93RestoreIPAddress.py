class Solution(object):
    def restoreIpAddresses(self, s):
        if not s:
            return []
        if len(s) > 12:
            return []
        answer = []
        self.dfs(answer, s, '')
        final = []
        for each in answer:
            if each not in final:
                final.append(each)
        return final

    def dfs(self, answer, s, path):
        if not s and len(path.split('.')) == 5:
            answer.append('.'.join(path.split('.')[1:]))
            return
        for i in range(1,4):
            if s[:i] and 0 <= int(s[:i]) <= 255 and str(int(s[:i])) == s[:i]:
                self.dfs(answer, s[i:], path+'.'+s[:i])
