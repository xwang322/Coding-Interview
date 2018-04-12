class Solution(object):
    def readBinaryWatch(self, num):
        answer = []
        for x in range(1024):
            if bin(x).count('1') == num:
                h = x>>6
                m = x&0x3f
                if h <12 and m <60:
                    answer.append('%d:%02d' % (h,m))
        return answer