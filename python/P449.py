# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        answer = []
        def preOrder(node):
            if node:
                answer.append(node.val)
                preOrder(node.left)
                preOrder(node.right)
        preOrder(root)
        answer_str = [str(n) for n in answer] # cannot change the original one, have to redefine a new one
        '''
        def inOrder(node):
            if node:
                inOrder(node.left)
                answer.append(node.val)
                inOrder(node.right)
        inOrder(root)
        answer_str = [str(n) for n in answer]
        '''
        print answer_str
        return ' '.join(answer_str)
        

    def deserialize(self, data):
        vals = collections.deque(int(s) for s in data.split())
        def build(minval, maxval):
            if vals and minval<vals[0]<maxval:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = build(minval, val)
                node.right = build(val, maxval)
                return node
        return build(float('-infinity'), float('infinity'))
        #def buildIn(minval, maxval): cannot use inorder because no idea where the root is
        # for a BST, only preorder can recover it, not for inorder and postorder
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))