class Solution(object):
    def longestPalindrome(self, s):
        answer = ''
        length = 1
        for i in range(len(s)):
            temp = self.findLongestLength(s, i, i)
            if len(temp) > len(answer):
                answer = temp
            if i > 0:
                temp1 = self.findLongestLength(s, i-1, i)
                if len(temp1) > len(answer):
                    answer = temp1
        return answer

    def findLongestLength(self, s, left, right):
        while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
