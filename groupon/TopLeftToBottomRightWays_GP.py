/*
* 数组从top left走到bottom right多少种走法，有障碍，很简单秒了，然后讨论了一下dp和dfs做这题的优缺点，然后follow up从任何点走到终点的走法，只能用dfs了，没有写代码。
**/
# The dp solution is given in LC62, here is for DFS solution
# This is from the top left to bottom right, but can go back
def dfsUniquePath(m, n):
    if not m or not n:
        return 1
    answer = []
    visited = [[False for i in range(n)] for j in range(m)]
    dfs(answer, [], 0, 0, m, n, visited)
    return len(answer)

def dfs(answer, path, i, j, m, n, visited):
    if i == m-1 and j == n-1:
        if path not in answer:
            answer.append(path)
            return
    visited[i][j] = True
    if i+1 < m and not visited[i+1][j]:
        dfs(answer, path+[(i, j)], i+1, j, m, n, visited)
    if i-1 >= 0 and not visited[i-1][j]:
        dfs(answer, path+[(i, j)], i-1, j, m, n, visited)
    if j+1 < n and not visited[i][j+1]:
        dfs(answer, path+[(i, j)], i, j+1, m, n, visited)
    if j-1 >= 0 and not visited[i][j-1]:
        dfs(answer, path+[(i, j)], i, j-1, m, n, visited)
    visited[i][j] = False

answer = dfsUniquePath(3,7)
print answer

# This is the solution cannot go back, from (0,0) to (m-1, n-1)
def dfsUniquePath(m, n):
    if not m or not n:
        return 1
    answer = []
    visited = [[False for i in range(n)] for j in range(m)]
    dfs(answer, [], 0, 0, m, n, visited)
    return len(answer)

def dfs(answer, path, i, j, m, n, visited):
    if i == m-1 and j == n-1:
        if path not in answer:
            answer.append(path)
            return
    visited[i][j] = True
    if i+1 < m and not visited[i+1][j]:
        dfs(answer, path+[(i, j)], i+1, j, m, n, visited)
    if j+1 < n and not visited[i][j+1]:
        dfs(answer, path+[(i, j)], i, j+1, m, n, visited)
    visited[i][j] = False

answer = dfsUniquePath(4,11)
print answer

# This is for any starting point to the (m-1, n-1) can go back
def dfsUniquePath(i, j, m, n):
    if not m or not n:
        return 1
    answer = []
    visited = [[False for s in range(n)] for t in range(m)]
    dfs(answer, [], i, j, m, n, visited)
    return len(answer)

def dfs(answer, path, i, j, m, n, visited):
    if i == m-1 and j == n-1:
        if path not in answer:
            answer.append(path)
            return
    visited[i][j] = True
    if i+1 < m and not visited[i+1][j]:
        dfs(answer, path+[(i, j)], i+1, j, m, n, visited)
    if i-1 >= 0 and not visited[i-1][j]:
        dfs(answer, path+[(i, j)], i-1, j, m, n, visited)
    if j+1 < n and not visited[i][j+1]:
        dfs(answer, path+[(i, j)], i, j+1, m, n, visited)
    if j-1 >= 0 and not visited[i][j-1]:
        dfs(answer, path+[(i, j)], i, j-1, m, n, visited)
    visited[i][j] = False

answer = dfsUniquePath(2, 4, 3, 7)
print answer
