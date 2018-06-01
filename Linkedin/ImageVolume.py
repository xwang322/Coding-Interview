'''
题目：一个N dimention的image volume。interface里有两个函数，一个可以取得各维度的size，一个可以可以取得指定pixel的值。
编写程序求整个volume的和。 面试官是一个非常资深的白人，由于沟通和理解原因，这道题没有答的很圆满。
这题可以用recursive 和 non－recursive 两种方法答。
'''
# assume each dimension always starts from 0 to max size -1
# function getDims()
# function getPixel()

# use recursion
def imageVolume(image):
    if not image:
        return 0
    dimensions = getDims(image)
    candidates = []
    for dim in dimensions:
        candidates.append([i for i in range(dim)])
    n = len(candidates)
    coordinates = []
    dfs(coordinates, candidates, n, [])
    answer = 0
    for coor in coordinates:
        answer += getPixel(coor)
    return answer

def dfs(coordinates, candidates, n, path):
    if len(path) == n:
        coordinates.append(path)
        return
    for index, candidate in enumerate(candidates[0]):
        dfs(answer, candidates[1:], n, path+[candidate])


# use iteration
def imageVolume(image):
    if not image:
        return 0
    dimensions = getDims(image)
    candidates = []
    for dim in dimensions:
        candidate.append([i for i in range(dim)])
    coordinates = []
    n = len(dimensions)
    for i in range(n):
        if i == 0:
            temp = [[] for j in range(len(candidates[i]))]
            for index, each in enumerate(candidates[i]):
                temp[index] = [each]
        else:
            m = len(temp)
            current = len(candidates[i])
            tmp = [[] for j in range(current*m)]
            for j in range(m*current):
                tmp[j] = temp[j%m]
            for j in range(m*current):
                tmp[j].append(candidates[j/m])
            temp = tmp
    coordinates = temp
    answer = 0
    for coor in coordinates:
        answer += getPixel(coor)
    return answer    
