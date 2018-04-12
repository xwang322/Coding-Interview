class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return[0]
        connections = [] for i in range(n)
        for each in edges:
            connections[each[0]].append(each[1])
            connections[each[1]].append(each[0])
        