class Solution(object):
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0
        m = len(heightMap)
        n = len(heightMap[0])
        heap = []
        visited = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                print i, j
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = 1
        answer = 0
        while heap:
            height, i, j = heapq.heappop(heap)
            for x,y in ((i+1, j),(i-1, j),(i, j+1),(i, j-1)):
                if 0 <= x <= m-1 and 0 <= y <= n-1 and not visited[x][y]:
                    if heightMap[x][y] < height:
                        answer += (height - heightMap[x][y])
                        heapq.heappush(heap, (height, x, y))
                    else:
                        heapq.heappush(heap, (heightMap[x][y], x, y))
                    visited[x][y] = 1
        return answer

        
