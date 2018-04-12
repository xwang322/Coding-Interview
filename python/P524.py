class Solution(object):
    def findLongestWord(self, s, d):
        for string in sorted(d, key = lambda w: (-len(w), w)):
            it = iter(s)
            if all(c in it for c in string):
                return string
        return ''
            
        