class Solution(object):
    # for BFS method, directly will cause TLE, so using extend will be faster, be careful about extend function
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        queue = []
        answer = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    queue.append((i, j))
                    answer += 1
                    while queue:
                        row, col = queue.pop(0)
                        if 0<=row<m and 0<=col<n and grid[row][col] == '1':
                            grid[row][col] = '2'
                            queue.extend([(row+1, col), (row-1, col), (row, col+1), (row, col-1)])
        return answer
