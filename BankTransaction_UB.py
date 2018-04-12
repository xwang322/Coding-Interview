/*
* 第二轮，很搞笑了，紧张的等了好久没接到电话然后HR说interviewer有urgent matter，约了下周.. 
* 可能interviewer感到愧疚所以给了一道很简单的题：给了一些bank间transaction的数据，把两个一样的bank数据merge起来输出。
* 比如BOA->CHASE 20, CHASE->BOA 10, result就是 BOA->CHASE 10.
**/


def BankTransaction(records):
    if not records:
        return records
    dictionary = {}
    for record in records:
        dictionary[(record[0], record[1])] = dictionary.get((record[0], record[1]), 0) + record[2]
    answer = []
    for key in dictionary:
        for another in dictionary:
            if key[0] == another[1] and another[0] == key[1]:
                if dictionary[key] > dictionary[another]:
                    dictionary[key] = dictionary[key] - dictionary[another]
                    dictionary[another] = 0
                else:
                    dictionary[another] = dictionary[another] - dictionary[key]
                    dictionary[key] = 0
    for key in dictionary:
        if dictionary[key] != 0:
            answer.append(str(key[0])+'->'+str(key[1])+':'+str(dictionary[key]))
    return answer

answer = BankTransaction([['chase','BOA',20], ['BOA','chase',10], ['American','BOA',30], ['BOA','American',30], ['chase','BOA',40]])
print answer
