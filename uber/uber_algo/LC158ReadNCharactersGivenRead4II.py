# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.queue = []

    def read(self, buf, n):
        total = 0
        while self.queue and n > 0:
            buf[total] = self.queue.pop(0)
            total += 1
            n -= 1
        while n > 0:
            temp_buf = ['','','','']
            temp = read4(temp_buf)
            if not temp:
                return total
            if temp > n:
                self.queue += temp_buf[n:temp]
            for i in range(min(n, temp)):
                buf[total] = temp_buf[i]
                total += 1
                n -= 1
        return total
