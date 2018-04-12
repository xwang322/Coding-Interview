/*
* 店面：
* 就是lc的原题，克隆graph
**/

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        # BFS by one node in queue
        '''
        if not node:
            return None
        dictionary = {node: UndirectedGraphNode(node.label)}
        # use dictionary to keep track of visited
        queue = [node]
        while queue:
            element = queue.pop(0)
            if not dictionary[element]:
                dictionary[element] = UndirectedGraphNode(element.label)
            for neighbor in element.neighbors:
                if neighbor not in dictionary:
                    dictionary[neighbor] = UndirectedGraphNode(neighbor.label)
                    queue.append(neighbor)
                dictionary[element].neighbors.append(dictionary[neighbor])
        return dictionary[node]
        '''
        #DFS by one node in stack
        if not node:
            return None
        dictionary = {node: UndirectedGraphNode(node.label)}
        stack = [node]
        while stack:
            element = stack.pop()
            if not dictionary[element]:
                dictionary[element] = UndirectedGraphNode(element.label)
            for neighbor in element.neighbors:
                if neighbor not in dictionary:
                    dictionary[neighbor] = UndirectedGraphNode(neighbor.label)
                    stack.append(neighbor)
                dictionary[element].neighbors.append(dictionary[neighbor])
        return dictionary[node]
