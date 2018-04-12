class Solution(object):
    def reverseWords(self, string):
        if not string:
            return 
        string.append(" ")
        start = 0
        for i in range(len(string)):
            if string[i] == " ":
                self.tempReverse(start, i-1, string)
                start = i+1
        string.pop()
        return self.tempReverse(0, len(string)-1, string)
        
    def tempReverse(self, i, j, string):
        while i < j:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1