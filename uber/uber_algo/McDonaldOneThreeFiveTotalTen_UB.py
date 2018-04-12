/*
* 如果你去麦当劳，汉堡薯条可乐分别5，3，1，你只有十块钱，问你你可以买到的所有的东西的组合。
* 类似于combination sum。
* 写得比较快，于是最后又尬聊了很久。还是提前面完了。
**/

def McDonald(total, choices):
    if not total or not choices:
        return []
    choices.sort()
    answer = []
    dfs(total, choices, [], answer)
    final = []
    for each in answer:
        if sorted(each) not in final:
            final.append(sorted(each))
    return final

def dfs(total, choices, path, answer):
    if sum(path) == total:
        answer.append(path)
        return
    elif sum(path) > total:
        return
    for choice in choices:
        dfs(total, choices, path+[choice], answer)

answer = McDonald(10, [1, 3, 5])
print answer
