class Solution(object):
    def longestPalindrome(self, s):
        count = collections.Counter(s)
        answer = 0
        odd = 0
        for c in count:
            answer += count[c]
            if count[c] %2 == 1:
                answer -= 1
                odd += 1
        return answer+(odd>0)
                
        