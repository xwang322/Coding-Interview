class Solution(object):
    # bfs
    def pacificAtlantic(self, matrix):
        m = len(matrix)
        if m:
            n = len(matrix[0])
        else:
            n = 0
        if m*n == 0:
            return []
        top = [(0, i) for i in range(n)]
        left = [(i, 0) for i in range(m)]
        pacific = set(top+left)
        bottom = [(m-1, i) for i in range(n)]
        right = [(i, n-1) for i in range(m)]
        altantic = set(bottom+right)
        def bfs(vset):
            dz = zip((1, 0, -1, 0), (0, 1, 0, -1))
            curr_list = list(vset)
            while curr_list:
                dx, dy = curr_list.pop(0)
                for each in dz:
                    new_x, new_y = dx+each[0], dy+each[1]
                    if 0 <= new_x < m and 0 <= new_y < n:
                        if matrix[new_x][new_y] >= matrix[dx][dy]:
                            if (new_x, new_y) not in vset:
                                curr_list.append((new_x, new_y))
                                vset.add((new_x, new_y))
            
        bfs(altantic)
        bfs(pacific)
        result = altantic & pacific
        return map(list, result)
        