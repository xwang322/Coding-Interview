class Solution(object):
    def replaceWords(self, dict, sentence):
        sentencelist = sentence.split()
        for i in range(len(sentencelist)):
            for j in dict:
                if sentencelist[i].startswith(j):
                    sentencelist[i] = j
        return ' '.join(sentencelist)
        