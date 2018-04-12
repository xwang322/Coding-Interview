/*
* Given a matrix, with values 'W', 'G', '0', 'W' means wall, 'G' means Guard, 0 means the way you can go.
* Find the distance of all points to nearest guard.
* LC 542 变种。
**/
def findNearestGuard(matrix):
    if not matrix or not matrix[0]:
        return matrix
    m = len(matrix)
    n = len(matrix[0])
    stack = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 'G':
                stack.append((i, j))
    level = 1
    next_level = []
    while stack:
        while stack:
            a, b = stack.pop(0)
            if 0<=a+1<=m-1 and 0<=b<=n-1 and matrix[a+1][b] == '0':
                matrix[a+1][b] = level
                next_level.append((a+1, b))
            if 0<=a-1<=m-1 and 0<=b<=n-1 and matrix[a-1][b] == '0':
                matrix[a-1][b] = level
                next_level.append((a-1, b))
            if 0<=a<=m-1 and 0<=b+1<=n-1 and matrix[a][b+1] == '0':
                matrix[a][b+1] = level
                next_level.append((a, b+1))
            if 0<=a<=m-1 and 0<=b-1<=n-1 and matrix[a][b-1] == '0':
                matrix[a][b-1] = level
                next_level.append((a, b-1))
        stack = next_level
        next_level = []
        level += 1
    return matrix

matrix = findNearestGuard([['W','G','W'],['0','0','0'],['0','0','G']])
print matrix
