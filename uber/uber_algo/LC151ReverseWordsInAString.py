class Solution(object):
    def reverseWords(self, s):
        return ' '.join(list(s.strip().split())[::-1])
