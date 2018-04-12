class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return '1'
        s = '1'
        while n > 1:
            count = 0
            pivot = s[0]
            temp = ''
            for char in s:
                if char == pivot:
                    count += 1
                else:
                    temp += str(count) + pivot
                    pivot = char
                    count = 1
            temp += str(count) + pivot
            s = temp
            n -= 1
        return s
        
                    