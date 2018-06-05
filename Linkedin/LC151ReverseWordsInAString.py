class Solution(object):
    def reverseWords(self, s):
        if not s:
            return ''
        s.strip()
        slist = s.split()
        answer = ''
        for each in slist[::-1]:
            answer += each
            answer += ' '
        return answer[:-1]