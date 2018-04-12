class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        self.trie = {}
        self.lookup = ''
        for index, sentence in enumerate(sentences):
            self.addToTrie(sentence, times[index])

    def addToTrie(self, sentence, time):
        t = self.trie
        for char in sentence:
            if char not in t:
                t[char] = {}
            t = t[char]
        if '*' not in t:
            t['*'] = (-time, sentence)
        else:
            t['*'] = (t['*'][0]-time, sentence)

    def input(self, c):
        answer = []
        if c != '#':
            self.lookup += c
            answer += self.search(self.lookup)
            return [item[1] for item in sorted(answer)[:3]]
        else:
            self.addToTrie(self.lookup, 1)
            self.lookup = ''
            return answer

    def search(self, lookup):
        t = self.trie
        for char in self.lookup:
            if char not in t:
                return []
            t = t[char]
        return self.dfs(t)

    def dfs(self, t):
        answer = []
        if '*' in t:
            answer.append(t['*'])
        for key in t:
            if key != '*':
                answer.extend(self.dfs(t[key]))
        return answer


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
