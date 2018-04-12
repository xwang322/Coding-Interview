class Solution(object):
    def firstUniqChar(self, s):
        if not s:
            return -1
        counts = collections.Counter(s)
        for index, char in enumerate(s):
            if counts[char] == 1:
                return index
        return -1
