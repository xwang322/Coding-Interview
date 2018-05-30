'''
find celebrity变种。不一样的地方就是没有给knows这个API。给的是一个boolean二维数组A。A[j]如果是true，那么说明i follow j。
根据数组A，返回一个int所有人都follow他，但是他不follow任何人。
'''

def findCelebrity(array):
    # assume somebody must know himself/herself
    n = len(array)
    for i in range(n):
        if not any(array[i][:i] + array[i][i+1:]):
            flag = True
            for j in range(n):
                if not array[j][i]:
                    flag = False
                    break
            if flag:
                return i
    return -1

answer = findCelebrity([[1,0,1,0],[0,0,1,0],[0,0,1,0],[0,0,1,1]])
print answer
