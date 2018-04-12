class Solution(object):
    def reverseString(self, s):
        answer = list(s)
        answer1 = answer[::-1]
        return ''.join(answer1)
        