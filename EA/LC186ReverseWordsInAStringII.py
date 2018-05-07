class Solution(object):
    # input is a char array, not a strict string
    def reverseWords(self, string):
        if not string:
            return
        string.append(' ')
        start = 0
        i = 0
        while i < len(string):
            if string[i] == ' ':
                self._swap(string, start, i-1)
                start = i+1
            i += 1
        string.pop()
        print len(string)
        self._swap(string, 0, len(string)-1)

    def _swap(self, string, start, end):
        while start < end:
            string[start], string[end] = string[end], string[start]
            start += 1
            end -= 1
