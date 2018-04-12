class Solution(object):
    def findSubstring(self, s, words):
        wordsdict = {}
        wordlength = len(words[0])
        wordnum = len(words)
        answer = []
        for i in words:
            if i not in wordsdict:
                wordsdict[i] = 1
            else:
                wordsdict[i] += 1
        answer = []
        for i in range(len(s)+1-wordlength*wordnum):
            tempdict = {}
            j = 0
            while j < wordnum:
                check_word = s[i+j*wordlength : i+j*wordlength+wordlength]
                if check_word not in wordsdict:
                    break
                if check_word not in tempdict:
                    tempdict[check_word] = 1
                else:
                    tempdict[check_word] += 1
                if tempdict[check_word] > wordsdict[check_word]:
                    break
                j += 1
            if j == wordnum:
                answer.append(i)
        return answer