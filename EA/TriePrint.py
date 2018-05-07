'''
第二题是关于Trie的，已经实现好了Trie的add, search，实现按字母顺序的打印，我是用DFS和back tracking来做的。
'''
class TrieNode(object):
    def __init__(self):
        self.dict = {}
        self.isWord = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        t = self.root
        for char in word:
            if char not in t.dict:
                t.dict[char] = TrieNode()
            t = t.dict[char]
        t.isWord = True

    def search(self, word):
        return self.find(self.root, word)

    def find(self, node, word):
        if not word:
            return node.isWord
        if word[0] == '.':
            for each in node.dict:
                if self.find(node.dict[each], word[1:]):
                    return True
        else:
            temp = node.dict.get(word[0])
            if temp:
                return self.find(temp, word[1:])
        return False

    def printWordDictionary(self):
        sortedList = []
        for key in self.root.dict:
            self.dfs(self.root.dict[key], key, sortedList, '')
        sortedList.sort()
        return sortedList

    def dfs(self, node, key, answer, path):
        path += key
        if node.isWord:
            answer.append(path)
        for temp in node.dict:
            self.dfs(node.dict[temp], temp, answer, path)
            
obj = WordDictionary()
obj.addWord('bad')
obj.addWord('bac')
obj.addWord('beg')
obj.addWord('die')
obj.addWord('mad')
print obj.search('bad')
print obj.search('.ad')
print obj.search('mac')
print obj.search('ma.')
print obj.printWordDictionary()
