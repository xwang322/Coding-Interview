class Solution(object):
    def longestPalindrome(self, s):
        counter = collections.Counter(s)
        answer = 0
        flag = False
        for key in counter:
            if not counter[key]%2:
                answer += counter[key]
            else:
                answer += counter[key]-1
                flag = True
        if flag:
            answer += 1
        return answer