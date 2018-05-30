class Solution(object):
    def intToRoman(self, num):
        dictionary = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        answer = ''
        divider = 1000
        while num:
            part = num/divider
            remainder = num%divider
            if part == 9:
                answer += dictionary[divider] + dictionary[divider*10]
            elif part == 4:
                answer += dictionary[divider] + dictionary[divider*5]
            else:
                if part >= 5:
                    answer += dictionary[divider*5]
                    part -= 5
                    print answer
                if 1<= part < 4:
                    while part:
                        answer += dictionary[divider]
                        part -= 1
            divider /= 10
            num = remainder
        return answer
