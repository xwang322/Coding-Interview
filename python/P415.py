class Solution(object):
    def addStrings(self, num1, num2):
        answer = []
        list1 = list(num1)
        list2 = list(num2)
        carry = 0
        while len(list1) > 0 or len(list2) > 0:
            if len(list1) > 0:
                temp1 = ord(list1.pop())-ord('0')
            else:
                temp1 = 0
            if len(list2) > 0:
                temp2 = ord(list2.pop())-ord('0')
            else:
                temp2 = 0
            answer.append((temp1+temp2+carry)%10)
            if temp1+temp2+carry >= 10:
                carry = (temp1+temp2+carry)/10
            else:
                carry = 0
        if carry:
            answer.append(carry)
        return ''.join(str(i) for i in answer[::-1])
