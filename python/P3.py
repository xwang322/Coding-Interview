class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = 0
        maxlength = 0
        dictionary = {}
        for i in range(len(s)):
            if s[i] in dictionary and start <= dictionary[s[i]]:
                start = dictionary[s[i]]+1
            else:
                maxlength = max(maxlength, i-start+1)
            dictionary[s[i]] = i
        return maxlength
        