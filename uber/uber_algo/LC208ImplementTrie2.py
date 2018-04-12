class Trie(object):

    def __init__(self):
        self.dictionary = {}


    def insert(self, word):
        t = self.dictionary
        for char in word:
            if char not in t:
                t[char] = {}
            t = t[char]
        t['#'] = '#'


    def search(self, word):
        t = self.dictionary
        for char in word:
            if char not in t:
                return False
            t = t[char]
        if '#' in t:
            return True
        else:
            return False

    def startsWith(self, prefix):
        t = self.dictionary
        for char in prefix:
            if char not in t:
                return False
            t = t[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
