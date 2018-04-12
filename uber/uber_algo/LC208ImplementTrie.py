class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                child = TrieNode()
                node.children[char] = child
                node = child
            else:
                node = node.children[char]
        node.isWord = True

    def search(self, word):
        node = self.root
        for char in word:
            node = node.children.get(char)
            if not node:
                return False
        return node.isWord
        

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            node = node.children.get(char)
            if not node:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)