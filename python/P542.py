class Solution(object):
    def updateMatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        answer = [[0 for i in range(n)] for j in range(m)]
        curr_list = [(i,j) for i in range(m) for j in range(n) if matrix[i][j]]
        step = 0
        while curr_list:
            step += 1
            next_level = []
            curr_change = []
            for every in curr_list:
                flag = False
                dz = zip((1, 0, -1, 0), (0, 1, 0, -1))
                for each in dz:
                    new_x = every[0]+each[0]
                    new_y = every[1]+each[1]
                    if 0 <= new_x < m and 0 <= new_y < n and matrix[new_x][new_y] == 0:
                        flag = True
                if flag:
                    answer[every[0]][every[1]] = step
                    curr_change.append(every)
                else:
                    next_level.append(every)
            for each in curr_change:
                matrix[each[0]][each[1]] = 0
            curr_list = next_level
        return answer
                    
            
            