class Solution(object):
    def multiply(self, num1, num2):
        if int(num1) == 0 or int(num2) == 0:
            return '0'
        answer = [0]*(len(num1)+len(num2))
        for i, n1 in enumerate(num1[::-1]):
            for j, n2 in enumerate(num2[::-1]):
                answer[len(answer)-i-j-1] += (int(n1)*int(n2))%10
                answer[len(answer)-i-j-2] += (int(n1)*int(n2))/10
        i = len(answer)-1
        while i >= 0:
            if answer[i] > 9:
                answer[i-1] += answer[i]/10
                answer[i] = answer[i]%10
            i -= 1
        answer.reverse()
        while answer[-1] == 0:
            answer.pop()
        answer.reverse()
        return ''.join(str(each) for each in answer)