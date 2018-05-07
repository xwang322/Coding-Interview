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

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
