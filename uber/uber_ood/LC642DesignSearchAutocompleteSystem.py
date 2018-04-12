class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.data = None
        self.rank = 0

class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        self.trie = TrieNode()
        self.keyword = ''
        for index, sentence in enumerate(sentences):
            self.addToTrie(sentence, times[index])

    def addToTrie(self, sentence, time):
        root = self.trie
        for char in sentence:
            if char not in root.children:
                root.children[char] = TrieNode()
            root = root.children[char]
        root.isWord = True
        root.data = sentence
        root.rank -= time

    def input(self, c):
        answer = []
        if c != '#':
            self.keyword += c
            answer += self.search(self.keyword)
        else:
            self.addToTrie(self.keyword, 1)
            self.keyword = ''
        return [item[1] for item in sorted(answer)[:3]]

    def search(self, keywords):
        root = self.trie
        for char in keywords:
            if char not in root.children:
                return []
            root = root.children[char]
        return self.dfs(root)

    def dfs(self, root):
        answer = []
        if root.isWord:
            answer.append((root.rank, root.data))
        for child in root.children:
            answer.extend(self.dfs(root.children[child]))
        return answer

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
