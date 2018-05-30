'''
输入是一个array stream，在任何时候call你的method，给一个input value，让返回之前输入过的数字有没有两个加起来等于这个value的（2sum稍稍变形）
'''
class Soution(object):

    def  __init__(self):
        self.dictionary = {}

    def record(self, value):
        self.dictionary[value] = self.dictionary.get(value, 0) + 1

    def Next(self):
        if self.hasNext():
            self.record(self.Next())

    def targetVisited(self, target):
        for key in self.dictionary:
            if target - key in self.dictionary:
                if target - key == key:
                    return self.ditionary[key] >= 2
                else:
                    return True
        return False
