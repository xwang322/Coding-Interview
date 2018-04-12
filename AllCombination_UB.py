/*
* 发一个昨天新鲜的uber电面，最后没调试通，感觉挂了攒人品吧
* 有n个list，假设平均长度是m，每个必须出一个元素，要求输出所有的可能的组合
* 例如输入{a,b}, {c,d}, {e,f}
* 则要输出{a,c,e}, {a,c,f}, {a,d,e}, {a,d,f},{b,c,e},{b,c,f},{b,d,e},{b,d,f}
* 最基础方法肯定是每个list循环一次，时间复杂度过大为m^n，面试官要求更优解，然后写了recursive解法，应该能达到m＊n？？不太确定，准备move on了，祝大家求职顺利
**/
def AllCombination(lists):
    if not lists:
        return []
    answer = []
    length = len(lists)
    dfs(answer, lists, 0, length, [])
    return answer

def dfs(answer, lists, index, length, path):
    if len(path) == length:
        answer.append(path)
        return
    for i in range(index, length):
        for element in lists[i]:
            dfs(answer, lists, i+1, length, path+[element])

answer = AllCombination([['a','b'],['c','d'],['e','f']])
print answer
