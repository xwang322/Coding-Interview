/*
* Jungle Book
*
* 输入是一个list,index代表pray,value代表predator,value = -1 代表没有predator,
* 就是说list = <n个有向edge, n个node的tree(forest),题里说输入满足不成环,一个species只有一个predator。
* 问把这些动物最少分成几组，使组内成员不互相伤害(A->B->C的话A,C也不能一组)
* */
def JungleBook(books):
    count = 0
    dictionary = {}
    for i in range(len(books)):
        count = max(count, calculate(books, i, dictionary))
    return count

def calculate(books, index, dictionary):
    predator = books[index]
    if predator == -1:
        dictionary[index] = 1
        return 1
    value = 0
    if predator in dictionary:
        value = dictionary[predator] + 1
    else:
        value = calculate(books, predator, dictionary) + 1
    dictionary[index] = value
    return value
