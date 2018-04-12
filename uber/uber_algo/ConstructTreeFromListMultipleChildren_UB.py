/*
* 发个前两天面的Uber攒人品，可爱的菲律宾小姐姐面的给一个list,
* 每个元素(A, B) 代表A是B的父节点，构建整棵树并输出父节点, 随后又问了如果不止一棵树返回多个root，判断是否valid等。
**/
# this one not implemented by CoderPad for hard to implement
# Binary Tree but not BST, so just the same strategy in LC 207 to check if there is a valid root, if null, what to do, if multiple, what to do
class TreeNode(object):
    def __init__(self, x, children = []):
        self.val = x
        self.children = []

def ValidTree(lists):
    if not lists:
        return False
    nodes = []
    for each in lists:
        if each[0] not in nodes:
            nodes.append(ord(each[0])-ord('A'))
        if each[1] not in nodes:
            nodes.append(ord(each[1])-ord('A'))
    number = len(nodes)
    degress = [0]*number
    # check if there is a node with 0 degree
    for each in lists:
        degree[each[1]] += 1
    if 0 not in degree:
        return False # not a valid root
    elif degree.count(0) > 1:
        return False # too many roots
    else:
        root = None
        queue = []
        for index, value in enumerate(degree):
            if value == 0:
                root = index
                queue.append(index)
                break
        root = TreeNode(ord('A')+queue[0])
        i = 0
        while queue:
            parent = queue.pop(0)
            node = None
            if i > 1:
                node = TreeNode(parent)
            else:
                node = root
            for each in lists:
                if ord(each[0])-ord('A') == parent:
                     degree[ord(each[1])-ord('A')] -= 1
                     child = TreeNode(each[1])
                     node.children.append(child)
                     if degree[ord(each[1])-ord('A')] == 0:
                         queue.append(ord(each[1])-ord('A'))
            i+= 1
        return root
