# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        self.data = []
        self.index = 0
        self._getlist(nestedList)

    def _getlist(self, nestedList):
        for item in nestedList:
            if item.isInteger():
                self.data.append(item.getInteger())
            else:
                self._getlist(item.getList())
        
    def next(self):
        answer = self.data[self.index]
        self.index += 1
        return answer

    def hasNext(self):
        if(self.index<len(self.data)):
            return True
        return False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())