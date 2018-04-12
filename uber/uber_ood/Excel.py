'''
Dessign excel
这里问的很细，比如每个cell的value可以分为numeric，string和formula，
而formula又是另外一个object，需要考虑parameter的个数和种类，parameter是否valid，还有evaluate方法的实现。
还有就是用什么方式存储sheet，一种方式是hash map，但是更新会很麻烦比如删除一整行，那么这一行后边的数据都要更新，
另一种是用类似linked list的方式，但如果是sparse matrix会很浪费空间或者很难实现，算是有trade off
Related link: http://massivetechinterview.blogspot.com/2015/09/design-excel.html
http://www.1point3acres.com/bbs/thread-132725-1-1.html
http://www.1point3acres.com/bbs/thread-140449-1-1.html
Analysis: OOD, initial is OK, needs to consider how to refer to other cells, how to modify whole col based data, how to store images?
Basic idea: first enable two functions: set and get
Follow up: for image, stores at file system, probably HDFS, then the dict stores a directory path
Some defined functions: SaveToFS(), FetchInFS()
'''
# Assume the excel is 0-index
import collections
import os
class Formula(object):
    def __init__(self, formula):
        if formula[0] != '=':
            print 'Not a valid formula expression'
        self.formula = formula[1:]

class Excel(object):
    def __init__(self):
        self.largestRow = 65535
        self.RowDict = collections.defaultdict(defaultdict)
        self.ColDict = collections.defaultdict(defaultdict)
        self.dependency = collections.defaultdict(list)

    def set(self, row, col, value):
        if not row or not col:
            return
        if row > self.largestRow:
            return
        if row not in self.RowDict:
            self.RowDict[row] = {}
            if col not in self.RowDict[row]:
                self.RowDict[row][col] = {}
        if col not in self.ColDict:
            self.ColDict[col] = {}
            if row not in self.ColDict[col]:
                self.ColDict[col][row] = {}
        savepath = None
        if value[0] != '=':
            if not isinstance(value, int) and not isinstance(value, string) and isinstance(value, float):
                savepath = os.path.dirname(SaveToFS(value))
                self.RowDict[row][col] = savepath
                self.ColDict[col][row] = savepath
            else:
                self.RowDict[row][col] = value
                self.ColDict[col][row] = value
        else:
            formula_value = self.calculate(value[1:])
            self.RowDict[row][col] = formula_value
            self.ColDict[col][row] = formula_value
            depency_list = self.getDependency(value[1:])
            self.dependency[(row, col)] = depency_list

    def getDependency(self, expression):
        level = {'+':1, '-':1, '*':2, '/':2, '(':0, ')':0}
        answer = []
        for i in re.compile('\d+|[()+-/\*]').findall(expression):
            if i not in level:
                answer.append(self.ExcelSheet(i))
        return answer

    def calculate(self, formula):
        op_stack = []
        num_stack = []
        level = {'+':1, '-':1, '*':2, '/':2, '(':0, ')':0}
        for i in re.compile('\d+|[()+-/\*]').findall(formula):
            if i in level:
                if len(op_stack) == 0 or i == '(' or level[i] > level[op_stack[-1]]:
                    op_stack.append(i)
                elif i == ')':
                    while op_stack[-1] != '(':
                        num_stack.append(self.cal(num_stack.pop(), num_stack.pop(), op_stack.pop()))
                    op_stack.pop()
                elif level[i] <= level[op_stack[-1]]:
                    num_stack.append(self.cal(num_stack.pop(), num_stack.pop(), op_stack.pop()))
                    op_stack.append(i)
            else:
                num_stack.append(self.convert(i))
        while len(op_stack) != 0:
            num_stack.append(self.cal(num_stack.pop(), num_stack.pop(), op_stack.pop()))
        return num_stack[0]

    def cal(self, num1, num2, operator):
        if operator == '+':
            return num1+num2
        elif operator == '-':
            return num2-num1
        elif operator == '*':
            return num2*num1
        elif operator == '/':
            return num2//num1

    def convert(self, expression):
        if not expression:
            return None
        for i in range(len(expression)):
            if expression[:i].isalpha() and expression[i:].isdigit():
                temp = self.ExcelSheet(expression[:i])
                return self.RowDict[int(expression[i:])-1][temp]

    def ExcelSheet(self, letters):
        if not letters:
            return None
        answer = 0
        for i in range(len(letters)):
            digit = len(letters)-1-i
            answer = (26**digit)*(ord(letters[i])-ord('A'))
        return answer

    def get(self, row, col):
        if not row or not col:
            return None
        if row > self.largestRow:
            return 'No such row exists.'
        temp1 = self.RowDict[row][col]
        temp2 = self.ColDict[col][row]
        if temp1 == temp2:
            if isinstance(temp1, int) or isinstance(temp1, string) or isinstance(temp1, float):
                return temp1
            else:
                return FetchInFS(temp1)
        return 'Data is not consistent, needs to check the data.'

    def updateCol(self, col, action):
        # action could be 2 types: add and delete, 0 for delete, 1 for add
        if not col:
            return
        tempdictionary = sorted(self.ColDict, reverse = True)
        if not action:
            for row in tempdictionary[col]:
                if self.dependency[row][col]:
                    self.dfsdelete((row, col))
                    del self.dependency[row][col]
            del tempdictionary[col]
            self.ColDict = tempdictionary
        else:
            for key in tempdictionary:
                if key >= col:
                    tempdictionary[key+1] = tempdictionary[key]
                    del tempdictionary[key]
            tempdictionary[col] = {}
            self.ColDict = tempdictionary

    def updateCRow(self, row, action):
        # action could be 2 types: add and delete, 0 for delete, 1 for add
        if not row:
            return
        if row > self.largestRow:
            return 'No such row exists.'
        tempdictionary = sorted(self.RowDict, reverse = True)
        if not action:
            for col in tempdictionary[row]:
                if self.dependency[row][col]:
                    self.dfsdelete((row, col))
                    del self.dependency((row, col))
            del tempdictionary[row]
            self.RowDict = tempdictionary
        else:
            for key in tempdictionary:
                if key >= row:
                    if key + 1 <= self.largestRow:
                        tempdictionary[key+1] = tempdictionary[key]
                        del tempdictionary[key]
            tempdictionary[row] = {}
            self.RowDict = tempdictionary
