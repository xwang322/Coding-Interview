class Solution(object):
    def exclusiveTime(self, n, logs):           
        answer = [0] * n
        stack = []
        temp = 0
        for log in logs:
            items = log.split(':')
            fn, typ, time = int(items[0]), items[1], int(items[2])
            if not stack:
                stack.append(fn)
                temp = time
            elif typ == 'start' and stack:
                answer[stack[-1]] += time-temp
                temp = time
                stack.append(fn)
            elif typ == 'end':
                answer[stack.pop()] += time-temp+1
                temp = time+1
        return answer
            