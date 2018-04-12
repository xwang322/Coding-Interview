/*
* 第一题 flattern a json, 输入
*｛
* 'a': '3',
* 'b': '4',
* 'c': {
* 'd': '5',
* 'e': '6'
* }
* ｝
* 输出
* ｛
* 'a': '3',
* 'b': '4',
* 'c.d': '5',
* 'c.d': '6'
｝
**/
class NestedJsonIterator(object):
    def __init__(self, nestedList):
        self.nestedList = nestedList
        self.answer = {}
        for key in self.nestedList:
            if type(self.nestedList[key]) is str:
                self.answer[key] = self.nestedList[key]
            else:
                temp = NestedJsonIterator(self.nestedList[key])
                while temp.hasNext():
                    self.answer[key+'.'+temp.answer.keys()[-1]] = temp.answer[temp.answer.keys()[-1]]
                    temp.answer.pop(temp.answer.keys()[-1])
        print self.answer

    def hasNext(self):
        if self.answer:
            return True
        return False

NestedJsonIterator({'a':'3', 'b':'4', 'c':{'d':{'e':'5'}, 'n':{'m':'45'}}, 'g':{'h':{'j':'10'}}})  
