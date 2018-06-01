'''
第二题给定一个m*n的grid，上面有一些点代表一群人的位置，找最近的meet point
'''
def meetNearestPoint(grid, start):
    if not grid:
        return [-1, -1]
    m = len(grid)
    n = len(grid[0])
    if not 0 <= start[0] < m or not 0 <= start[1] < n:
        return [-1, -1]
    queue = [start]
    visited = set()
    while queue:
        coordinate = queue.pop(0)
        x = coordinate[0]
        y = coordinate[1]
        if (x,y) in visited:
            continue
        if grid[x][y] == 1:
            return [x,y]
        if x-1 >= 0:
            queue.append((x-1, y))
        if x+1 < m:
            queue.append((x+1, y))
        if y-1 >= 0:
            queue.append((x, y-1))
        if y+1 < n:
            queue.append((x, y+1))
    return [-1, -1]

answer = meetNearestPoint([[0, 0, 0, 1],[1, 0, 0, 1],[0, 1, 0, 0],[1, 0, 0, 0]], [1,0])
print answer
