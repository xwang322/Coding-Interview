/*
* Clone the Graph
*要写verification，这里比较tricky，如果直接是写比较两个graph是否相同，可能又回到了原本clone graph的道路上
* 最后还是在solution里加了helper function，把create的node全部存起来，然后做比较
*
* 我用了helper function，在new node的地方 把所有new的 结点放到一个vector里，然后在verification的时候把vector里的所有点和他的子节点打印出来
* 否则就是相当于重写原来的主code了，上面的那种helper function写法是给过的。
**/
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

def cloneGraphandVerification(node):
    if not node:
        return None
    dictionary = {node:UndirectedGraphNode(node.label)}
    queue = [node]
    verification = set()
    verification.add(dictionary[node])
    while queue:
        element = queue.pop(0)
        if not dictionary[element]:
            dictionary[element] = UndirectedGraphNode(element.label)
            verification.add(dictionary[element])
        for neighbor in element.neighbors:
            if neighbor not in dictionary:
                dictionary[neighbor] = UndirectedGraphNode(neighbor.label)
                queue.append(neighbor)
                verification.add(dictionary[neighbor])
            dictionary[element].neighbors.append(dictionary[neighbor])
    return dictionary[node]

def GraphVerification(node, verification, dictionary):
    if not node:
        return True
    queue_check = [node]
    while queue_check:
        element = queue_check.pop(0)
        if element.label not in verification:
            return False
        for neighbor in element.neighbors:
            queue_check.append(neighbor)
    return True
