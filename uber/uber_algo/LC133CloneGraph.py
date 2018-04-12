# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        # BFS
        ''''
        if not node:
            return None
        dictionary = {node: UndirectedGraphNode(node.label)}
        queue = collections.deque([(node, dictionary[node])])
        while queue:
            element = queue.popleft()
            original, cloned = element[0], element[1]
            for v in original.neighbors:
                if v not in dictionary:
                    dictionary[v] = UndirectedGraphNode(v.label)
                    queue.append((v, dictionary[v]))
                cloned.neighbors.append(dictionary[v])
        return dictionary[node]
        '''
        #DFS
        if not node:
            return None
        dictionary = {node: UndirectedGraphNode(node.label)}
        stack = [node]
        while stack:
            temp = stack.pop()
            for neighbor in temp.neighbors:
                if neighbor not in dictionary:
                    copy = UndirectedGraphNode(neighbor.label)
                    dictionary[neighbor] = copy
                    dictionary[temp].neighbors.append(copy)
                    stack.append(neighbor)
                else:
                    dictionary[temp].neighbors.append(dictionary[neighbor])
        return dictionary[node]