'''
一id有多个电话号码，找出有哪些id属于同一个人，输出属于同一人的电话list，lc有这题忘了名字
'''
import collections
def UnionTelePerson(numbers):
    if not numbers:
        return []
    phones_to_id = collections.defaultdict(list)
    visited = [False] * len(numbers)
    answer = []
    for index, number in enumerate(numbers):
        for j in range(1, len(number)):
            telephone = number[j]
            phones_to_id[telephone].append(index)
    for index, number in enumerate(numbers):
        if visited[index]:
            continue
        temp = set()
        dfs(visited, numbers, index, temp, phones_to_id)
        answer.append([numbers[index][0]]+sorted(temp))
    return answer


def dfs(visited, numbers, index, temp, phones_to_id):
    if visited[index]:
        return
    visited[index] = True
    for j in range(1, len(numbers[index])):
        telephone = numbers[index][j]
        temp.add(telephone)
        for neighbor in phones_to_id[telephone]:
            dfs(visited, numbers, neighbor, temp, phones_to_id)

answer = UnionTelePerson([['bob','6085561914','6085561597','6087891524'],['alice', '7851267892'],['robert','6085561597'],['Susan', '3216549870'],['john bob','6085561597'],['Alice','7851267892'],['Emily','7851267892'],['Hagness', '3216549870']])
print answer
