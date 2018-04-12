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
        
