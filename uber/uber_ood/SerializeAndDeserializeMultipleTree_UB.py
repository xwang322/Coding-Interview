/*
* 李抠 二舅妻 变种, 要很多个孩子. 前半段写完了, run了没问题, 后半段在 debug 的时候说没时间了, 就没写完.
**/
# I think we need to know how many children at most can one TreeNode has， in this example, we have 3
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.child1 = None
        self.child2 = None
        self.child3 = None

class Codec:
    def serialize(self, root):
        if not root:
            return ' ,null'
        answer = ''
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            if not node:
                answer += ' ,null'
            else:
                answer += ','+str(node.val)
                queue.append(node.child1)
                queue.append(node.child2)
                queue.append(node.child3)
        return answer

    def deserialize(self, data):
        data = data.split(',')
        data.pop(0)
        value = data.pop(0)
        if value == 'null':
            root = None
        else:
            root = TreeNode(int(value))
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                value1, value2, value3 = data.pop(0), data.pop(0), data.pop(0)
                if value1 != 'null':
                    node.child1 = TreeNode(int(value1))
                else:
                    node.child1 = None
                if value2 != 'null':
                    node.child2 = TreeNode(int(value2))
                else:
                    node.child2 = None
                if value3 != 'null':
                    node.child3 = TreeNode(int(value3))
                else:
                    node.child3 = None
                queue.append(node.child1)
                queue.append(node.child2)
                queue.append(node.child3)
        return root
