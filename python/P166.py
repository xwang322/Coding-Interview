class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return '0'
        if denominator == 0:
            return 
        answer = []
        if numerator*denominator < 0:
            answer.append('-')
        num = abs(numerator)
        den = abs(denominator)
        inter = num//den
        num = num%den
        answer.append(str(inter))
        if num == 0:
            return ''.join(answer)
        answer.append('.')
        dic = {}
        while num:
            if num in dic:
                answer.insert(dic[num], '(')
                answer.append(')')
                break
            dic[num] = len(answer)
            inter, num = divmod(num*10, den)
            answer.append(str(inter))
        return ''.join(answer)