class Solution(object):
    def numberToWords(self, num):
        self.lessthan20 = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        self.bignumber = ['','Thousand','Million','Billion']
        self.tens = ['','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        if num == 0:
            return 'Zero'
        answer = ''
        for i in range(len(self.bignumber)):
            if num%1000:
                answer = self.Module(num%1000) + ' '+ self.bignumber[i] + ' ' + answer
            num /= 1000
        return ' '.join(answer.strip().split())

    def Module(self, number):
        if number >= 100:
            return self.lessthan20[number/100] + ' ' + 'Hundred' + ' '+ self.Module(number%100)
        elif 20 <= number < 100:
            return self.tens[number/10] + ' ' + self.lessthan20[number%10]
        elif 0 < number < 20:
            return self.lessthan20[number]
        else:
            return ''
