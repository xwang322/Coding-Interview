class Solution(object):
    def plusOne(self, digits):
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            carry, digits[i] = (digits[i]+carry)/10, (digits[i]+carry)%10
        answer = []
        if carry:
            answer = [carry]+digits
        else:
            answer = digits
        return answer
