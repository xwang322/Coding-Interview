class Solution(object):
    def reverseWords(self, s):
        s_list = s.split()
        return ' '.join(s_list[::-1])
