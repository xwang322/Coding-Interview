class Solution(object):
    def find(self, i, j, parent):
        if i != parent[i][j][0] or j != parent[i][j][1]:
            parent[i][j] = self.find(parent[i][j][0], parent[i][j][1], parent)
        return parent[i][j]

    def union(self, i1, j1, i2, j2, parent):
        root1 = self.find(i1, j1, parent)
        root2 = self.find(i2, j2, parent)
        if root1 == root2:
            return True
        parent[root1[0]][root1[1]] = (root2[0], root2[1])
        return False

    def numIslands2(self, m, n, positions):
        answer = []
        parent = [[(-1, -1) for i in range(n)]for j in range(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        num = 0
        for row, col in positions:
            parent[row][col] = (row, col)
            num += 1
            for direction in directions:
                i = row+direction[0]
                j = col+direction[1]
                if i < 0 or i >= m or j < 0 or j >= n or parent[i][j] == (-1, -1):
                    continue
                if not self.union(row, col, i, j, parent):
                    num -= 1
            answer.append(num)
        return answer
                
