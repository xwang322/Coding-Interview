class Solution(object):
    def toHex(self, num):
        answer = []
        strings = '0123456789abcdef'
        if num < 0:
            num += 0x100000000
        while num:
            answer.append(strings[num%16])
            num /= 16
        return ''.join(answer[::-1]) if answer else '0'
        