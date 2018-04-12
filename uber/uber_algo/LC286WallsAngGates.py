class Solution(object):
    def wallsAndGates(self, rooms):
        if not rooms or not rooms[0]:
            return
        m = len(rooms)
        n = len(rooms[0])
        temp = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    temp.append([i,j])
        level = 0
        next_level = []
        while temp:
            while temp:
                element = temp.pop()
                if 0<=element[0]-1<=m-2 and 0<=element[1]<=n-1:
                    if rooms[element[0]-1][element[1]] == 2147483647:
                        rooms[element[0]-1][element[1]] = level+1
                        next_level.append([element[0]-1, element[1]])
                if 1<=element[0]+1<=m-1 and 0<=element[1]<=n-1:
                    if rooms[element[0]+1][element[1]] == 2147483647:
                        rooms[element[0]+1][element[1]] = level+1
                        next_level.append([element[0]+1, element[1]])
                if 0<=element[0]<=m-1 and 0<=element[1]-1<=n-2:
                    if rooms[element[0]][element[1]-1] == 2147483647:
                        rooms[element[0]][element[1]-1] = level+1
                        next_level.append([element[0], element[1]-1])
                if 0<=element[0]<=m-1 and 1<=element[1]+1<=n-1:
                    if rooms[element[0]][element[1]+1] == 2147483647:
                        rooms[element[0]][element[1]+1] = level+1
                        next_level.append([element[0], element[1]+1])
            temp = next_level
            level += 1
            next_level = []



        
