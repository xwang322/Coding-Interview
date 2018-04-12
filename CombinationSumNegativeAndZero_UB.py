/*
* Uber 第一轮 国人大哥面我，combination sum。 唯一不同的是这个有负数，0.。。做出来了，run cases没问题。。。。
* 最后我SB说了一嘴，我见过一个类似的，只有正数。。。。。。。。我自己的锅，然后就挂了。。。。。
**/

def combinationSumAllRange(candidates, target):
    if not candidates or not target:
        return []
    candidates.sort()
    answer = []
    uplimit = 0
    downlimit = 0
    for candidate in candidates:
        if candidate > 0:
            uplimit += candidate
        elif candidate < 0:
            downlimit += candidate
    dfs(answer, candidates, target, [], uplimit, downlimit)
    final = []
    # depends on whether the output is duplicates allowed
    for each in answer:
        if each not in final:
            final.append(each)
    return final

def dfs(answer, candidates, target, path, uplimit, downlimit):
    if target == 0:
        answer.append(path)
    if target < downlimit:
        return
    elif target > uplimit:
        return
    for index, candidate in enumerate(candidates):
        dfs(answer, candidates[index+1:], target-candidate, path+[candidate], uplimit, downlimit)

answer = combinationSum2([-2, -1, 0, 1, 1, 2, 3], 3)
print answer
