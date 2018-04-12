class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        # DFS
        '''
        m = len(image)
        n = len(image[0])
        old_color = image[sr][sc]
        def dfs(image, row, col):
            if not (0 <= row < m and 0 <= col < n) or image[row][col] != old_color:
                return
            image[row][col] = newColor
            dfs(image, row+1, col);
            dfs(image, row-1, col);
            dfs(image, row, col+1);
            dfs(image, row, col-1);
        if old_color != newColor:
            dfs(image, sr, sc)
        return image
        '''
        #BFS
        m = len(image)
        n = len(image[0])
        old_color = image[sr][sc]
        this_level = []
        if old_color != newColor:
            this_level.append([sr, sc])
        next_level = []
        while this_level:
            while this_level:
                coordinate = this_level.pop(0)
                if 0<=coordinate[0]<m and 0<=coordinate[1]<n:
                    if image[coordinate[0]][coordinate[1]] == old_color:
                        image[coordinate[0]][coordinate[1]] = newColor
                        next_level.append([coordinate[0]+1, coordinate[1]]) 
                        next_level.append([coordinate[0]-1, coordinate[1]])
                        next_level.append([coordinate[0], coordinate[1]+1])
                        next_level.append([coordinate[0], coordinate[1]-1])
            this_level = next_level
            next_level = []
        return image
                        