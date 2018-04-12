class Solution(object):
    def findWords(self, words):
        keyboard = map(set, ['qwertyuiop', 'asdfghjkl', 'zxcvbnm'])
        answer = []
        for word in words:
            word_once = set(word.lower())
            if any(word_once <= oneset for oneset in keyboard):
                answer.append(word)
        return answer