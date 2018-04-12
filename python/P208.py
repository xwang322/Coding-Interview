class TriNode(object):
    def __init__(self):
        self.tnlst = dict()
        self.isword = False

class Trie(object):

    def __init__(self):
        self.root = TriNode()
        

    def insert(self, word):
        r = self.root
        for letter in word:
            if letter not in r.tnlst:
                r.tnlst[letter] = TriNode()
            r = r.tnlst[letter]
        r.isword = True

    def search(self, word):
        r = self.root
        for letter in word:
            if letter in r.tnlst:
                r = r.tnlst[letter]
            else:
                return False
        return r.isword
        

    def startsWith(self, prefix):
        r = self.root
        for letter in prefix:
            if letter in r.tnlst:
                r = r.tnlst[letter]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
                    