class Solution(object):
    def removeDuplicateLetters(self, s):
        # this python answer is not very good because result[-1:] is not clear
        index = {c:i for i, c in enumerate(s)}
        result = ''
        for i, c in enumerate(s):
            if c not in result:
                while c < result[-1:] and i < index[result[-1]]:
                    result = result[:-1]
                result += c
        return result
        