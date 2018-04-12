# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        i = 0
        while i < n:
            temp_buf = ['','','','']
            temp = read4(temp_buf)
            if not temp:
                break
            temp = min(temp, n-i)
            buf[i:] = temp_buf[:temp]
            i += temp
        return i
        
