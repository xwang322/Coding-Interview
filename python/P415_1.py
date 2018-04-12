class Solution(object):
    def addStrings(self, num1, num2):
        num1_l = list(num1)
        num2_l = list(num2)
        answer = []
        thisbit = 0
        nextbit = 0
        while len(num1_l) > 0 or len(num2_l) > 0:
            if len(num1_l) > 0:
                num1_b = ord(num1_l.pop())-ord('0')
            else:
                num1_b = 0
            if len(num2_l) > 0:
                num2_b = ord(num2_l.pop())-ord('0')
            else:
                num2_b = 0
            thisbit = (num1_b+num2_b+nextbit)%10
            nextbit = (num1_b+num2_b+nextbit)//10  #python / is float, // is floor
            answer.append(thisbit)
        if nextbit:
            answer.append(nextbit)
        return ''.join([str(i) for i in answer])[::-1]