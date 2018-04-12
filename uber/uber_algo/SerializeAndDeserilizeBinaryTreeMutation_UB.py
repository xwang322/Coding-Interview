'''
Serialize and deserialize a k-ary tree

意大利小哥，问的问题是encode and decode tree，也就是tree2string, string2tree。leetcode上貌似有原题，
但是不同的地方在于，leetcode上是binary tree，面试的时候我问了能不能假设tree是binary tree，他说不可以。。。
于是开始码，然后写test case，然后跑代码。。感觉思路是对的，但是跑出来结果总是不对，然后debug，
中间发现一个粗心大意的bug，解决后发现还有其他bug，也是各种试，最后在小哥的提醒下发现了有地方递归了两边。。
所以打印出来的东西总是double了。后也解决了，余下来五分钟聊天。这轮感觉不是很顺利，过程挺曲折的。

第三轮：coding，serialize/deserialize N-ary tree, 要求能handle各种类型的value，比如node的val可能是string，
或者其他什么的，总之就是要写成generic，反正我当时的意见就是node的val的type，必须支持serialiable这个借口，
也就是能把自己变成string，以及反过来。然后serialize的逻辑就是把child用括号包起来，就像这样Root(child 1)(child 2)...(child n)，
用recursion做，反过来就是处理括号，同样用递归做。
要求最后写test case，bug free。
'''
# The code is for 4-nary Tree
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.child1 = None
        self.child2 = None
        self.child3 = None
        self.child4 = None


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
                if isinstance(node.val, str):
                    answer += ',(str)' + node.val
                elif isinstance(node.val, int) or isinstance(node.val, float):
                    answer += ',' + str(node.val)
                queue.append(node.child1)
                queue.append(node.child2)
                queue.append(node.child3)
                queue.append(node.child4)
        return answer

    def deserialize(self, data):
        datalist = data.split(',')
        datalist.pop(0)
        if datalist and datalist[0] != 'null':
            if datalist[0].startwith('(str)'):
                root = TreeNode(datalist.pop(0)[5:])
            else:
                root = TreeNode(int(datalist.pop(0)))
        else:
            return None
        queue = [root]
        print datalist
        while queue:
            node = queue.pop(0)
            if node:
                temp1 = datalist.pop(0)
                temp2 = datalist.pop(0)
                temp3 = datalist.pop(0)
                temp4 = datalist.pop(0)
                if temp1 == 'null':
                    node.child1 = None
                else:
                    if node.child1.startwith('(str)'):
                        node.child1 = TreeNode(temp1[5:])
                    else:
                        node.child1 = TreeNode(int(temp1))
                    queue.append(node.child1)
                if temp2 == 'null':
                    node.child2 = None
                else:
                    if node.child2.startwith('(str)'):
                        node.child2 = TreeNode(temp2[5:])
                    else:
                        node.child2 = TreeNode(int(temp2))
                    queue.append(node.child2)
                if temp3 == 'null':
                    node.child3 = None
                else:
                    if node.child3.startwith('(str)'):
                        node.child3 = TreeNode(temp3[5:])
                    else:
                        node.child3 = TreeNode(int(temp3))
                    queue.append(node.child3)
                if temp4 == 'null':
                    node.child4 = None
                else:
                    if node.child4.startwith('(str)'):
                        node.child4 = TreeNode(temp4[5:])
                    else:
                        node.child4 = TreeNode(int(temp4))
                    queue.append(node.child4)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
