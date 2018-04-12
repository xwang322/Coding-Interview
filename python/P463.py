class Solution(object):
    def islandPerimeter(self, grid):
        if not grid or not grid[0]:
            return 0
        answer = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    answer += 4
                    if i >= 1:
                        if grid[i-1][j] == 1:
                            answer -= 2
                    if j >= 1:
                        if grid[i][j-1] == 1:
                            answer -= 2
        return answer