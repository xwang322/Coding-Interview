class Solution(object):
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        stack = []
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    stack.append((i,j))
                    count += 1
                    while stack:
                        a,b = stack.pop() #pop will be faster than pop(0)
                        if 0 <= a+1 <= m-1 and grid[a+1][b] == '1':
                            stack.append((a+1, b))
                        if 0 <= a-1 <= m-1 and grid[a-1][b] == '1':
                            stack.append((a-1, b))
                        if 0 <= b+1 <= n-1 and grid[a][b+1] == '1':
                            stack.append((a, b+1))
                        if 0 <= b-1 <= n-1 and grid[a][b-1] == '1':
                            stack.append((a, b-1))
                        grid[a][b] = '*'
        return count
