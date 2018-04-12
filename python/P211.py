class TrieNode():
    def __init__(self):
        self.childs = dict()
        self.isword = False


class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for letter in word:
            child = node.childs.get(letter)
            if child is None:
                child = TrieNode()
                node.childs[letter] = child
            node = child
        node.isword = True    

    def search(self, word):
        return self.find(self.root, word)
    
    def find(self, node, word):
        if word == '':
            return node.isword
        if word[0] == '.':
            for x in node.childs:
                if self.find(node.childs[x], word[1:]):
                    return True
        else:
            child = node.childs.get(word[0])
            if child:
                return self.find(child, word[1:])
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)