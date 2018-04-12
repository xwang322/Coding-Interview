class Solution(object):
    def islandPerimeter(self, grid):
        height = len(grid)
        width = len(grid[0])
        answer = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    answer += 4
                    if i>0 and grid[i-1][j] == 1:
                        answer -= 2
                    if j>0 and grid[i][j-1] == 1:
                        answer -= 2
        return answer
        