class Solution(object):
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        answer = 0
        stack = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    stack.append((i,j))
                    answer += 1
                    while stack:
                        row, col = stack.pop()
                        grid[row][col] = '2'
                        if row+1 <= m-1 and grid[row+1][col] == '1':
                            stack.append((row+1, col))
                        if row-1 >= 0 and grid[row-1][col] == '1':
                            stack.append((row-1, col))
                        if col+1 <= n-1 and grid[row][col+1] == '1':
                            stack.append((row, col+1))
                        if col-1 >= 0 and grid[row][col-1] == '1':
                            stack.append((row, col-1))
        return answer


        
