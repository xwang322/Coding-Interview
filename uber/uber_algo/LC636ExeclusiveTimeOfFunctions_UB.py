/*
* Implement a function return the exclusive running time of a function, given the function name and a list of logs.
* List<string> stands for a list of logs. The logs have the following structure:
* functionName StartOrEnd Time
* A start 10
* B start 11
* B end 12
* A end 20
* exclusive running time means the total running time of a function minus the total running time of its nested functions.
* for example, the exclusive running time of A = T(A) - T(B) T stands for the total running time of a fuction
* Func A{
* Func B();
* }
**/

class Solution(object):
    def exclusiveTime(self, n, logs):
        if not n or not logs:
            return []
        stack = []
        answer = [0]*n
        temp = 0
        for log in logs:
            log = log.split(':')
            functionName, ty, timestamp = int(log[0]), log[1], int(log[2])
            if not stack:
                stack.append(functionName)
                temp = timestamp
            elif ty == 'start':
                answer[stack[-1]] += timestamp-temp
                stack.append(functionName)
                temp = timestamp
            elif ty == 'end':
                answer[stack.pop()] += timestamp-temp+1
                temp = timestamp+1
        return answer
