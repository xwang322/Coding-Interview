/*
* 第二题write a function f(4) = four f(14) = fourteen f(123) = one hundred, twenty three f(12345) = twelve thousand, nine hundred, forty seven
**/
# similar to LC273, but needs to add comma in the output
lessthan20 = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
bignumber = ['','thousand,','million,','billion,']
tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
def NumberToEnglish(num):
    if num == 0:
        return 'Zero'
    answer = ''
    for i in range(len(bignumber)):
        if num%1000:
            answer = residual(num%1000) + ' ' + bignumber[i] + ' ' +  answer
        num /= 1000
    return answer

def residual(number):
    if 0 < number < 20:
        return lessthan20[number%20]
    elif 20 <= number <= 99:
        return tens[number/10]+' ' +lessthan20[number%10]
    elif 100 <= number:
        return lessthan20[number/100] + ' ' + 'hundred,' + ' ' + residual(number%100)
    else:
        return ''

answer = NumberToEnglish(68665893)
print answer
