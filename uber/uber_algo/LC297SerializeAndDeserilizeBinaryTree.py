# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        if not root:
            return ',null'
        queue = [root]
        answer = ''
        while queue:
            node = queue.pop(0)
            if not node:
                answer += ',null'
            else:
                answer += ',' + str(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return answer

    def deserialize(self, data):
        datalist = data.split(',')
        datalist.pop(0)
        if datalist and datalist[0] != 'null':
            root = TreeNode(int(datalist.pop(0)))
        else:
            return None
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                temp1 = datalist.pop(0)
                temp2 = datalist.pop(0)
                if temp1 == 'null':
                    node.left = None
                else:
                    node.left = TreeNode(int(temp1))
                    queue.append(node.left)
                if temp2 == 'null':
                    node.right = None
                else:
                    node.right = TreeNode(int(temp2))
                    queue.append(node.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
