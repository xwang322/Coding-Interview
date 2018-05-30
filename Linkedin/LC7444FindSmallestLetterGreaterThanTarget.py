class Solution(object):
    def nextGreatestLetter(self, letters, target):
        index = bisect.bisect_right(letters, target)
        if index == len(letters):
            return letters[0]
        else:
            return letters[index]
        
