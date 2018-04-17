class Solution(object):
    def leastBricks(self, wall):
        if not wall:
            return 0
        dictionary = {}
        for each in wall:
            length = 0
            for brick in each[:-1]:
                dictionary[length+brick] = dictionary.get(length+brick, 0)+1
                length += brick
        return len(wall) - max(dictionary.values()+[0])

class Solution(object):
    def leastBricks(self, walls):
        if not walls:
            return 0
        dictionary = {}
        for wall in walls:
            length = 0
            for brick in wall[:-1]:
                dictionary[length+brick] = dictionary.get(length+brick, 0)+1
                length += brick
        if not dictionary:
            return len(walls)
        else:
            return len(walls) - max(dictionary.values())

        
