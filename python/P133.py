# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # bfs
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        queue = []
        map = {}
        new = UndirectedGraphNode(node.label)
        queue.append(node)
        map[node] = new
        while queue:
            curr = queue.pop()
            for neighbor in curr.neighbors:
                if neighbor in map:
                    map[curr].neighbors.append(map[neighbor])
                else:
                    copy = UndirectedGraphNode(neighbor.label)
                    map[curr].neighbors.append(copy)
                    map[neighbor] = copy
                    queue.append(neighbor)
        return new