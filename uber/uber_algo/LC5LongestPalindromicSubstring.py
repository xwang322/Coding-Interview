class Solution(object):
    def longestPalindrome(self, s):
        if not string:
            return 0
        if len(s) == 1:
            return s
        maxlength = 0
        start = 0
        for i in range(len(s)):
            if s[i-maxlength:i+1] == s[i-maxlength:i+1][::-1]:
                start = i-maxlength
                maxlength += 1
            if i >= maxlength+1 and s[i-maxlength-1:i+1] == s[i-maxlength-1:i+1][::-1]:
                start = i-maxlength-1
                maxlength += 2
        return s[start:start+maxlength]

# This method will TLE
class Solution(object):
    def longestPalindrome(self, s):
        if not string:
            return 0
        if len(s) == 1:
            return s
        answer = [0 * i for i in range(len(s))]
        for i in range(len(s)-1):
            head = i
            j = len(s)-1
            step = 0
            while i < j:
                while i< j and s[j] != s[i]:
                    j -= 1
                temp = j
                while i < j and s[i] == s[j]:
                    i += 1
                    j -= 1
                    step += 2
                if i == j:
                    step += 1
                    answer[head] = step
                    break
                elif j+1 == i:
                    answer[head] = step
                    break
                else:
                    step = 0
                    j = temp-1
                    i = head
                answer[head] = step
        return s[answer.index(max(answer)):answer.index(max(answer))+max(answer)]
