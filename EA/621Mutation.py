'''
第二题某扣六而一的变种，变得简单了许多。所有的task的执行顺序不变。
相同tasks之间有一个constant的冷冻时间，输入 一个task序列，要求返回依次执行完所有tasks所花时间
'''
import collections
def followOrderedTask(tasks, constant):
    if not constant:
        return tasks
    counts = collections.Counter(tasks)
    dictionary = {}
    length = len(tasks)
    answer = 0
    i = 0
    while i < length:
        if tasks[i] not in dictionary:
            dictionary[tasks[i]] = i
        else:
            if i - dictionary[tasks[i]] >= constant:
                dictionary[tasks[i]] = i
            else:
                dictionary[tasks[i]] -= 1
                i -= 1
        i += 1
        answer += 1
        print dictionary
    return answer

answer = followOrderedTask(['A','B','C','A','B','C','A','B','C','A','B','C'], 3)
print answer
