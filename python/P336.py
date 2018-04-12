class Solution(object):
    def palindromePairs(self, words):
        words = {word:i for i,word in enumerate(words)}
        answer = []
        for word, k in words.iteritems():
            length = len(word)
            for j in range(length+1):
                prefix = word[:j]
                suffix = word[j:]
                if self.ispalindrome(prefix):
                    back = suffix[::-1]
                    if back in words and back != word:
                        answer.append([words[back], k])
                if self.ispalindrome(suffix) and j != length:
                    back = prefix[::-1]
                    if back in words and back != word:
                        answer.append([k, words[back]])
        return answer
        
        
    def ispalindrome(self, check):
        return check == check[::-1] # this is the best way to check palindrome