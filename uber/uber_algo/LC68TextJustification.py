class Solution(object):
    def fullJustify(self, words, maxWidth):
        text = ' '.join(words)+' '
        if text == ' ':
            return [' '*maxWidth]
        answer = []
        while text:
            idx = text.rfind(' ', 0, maxWidth+1)
            line = text[:idx].split()
            l, n = sum(len(w) for w in line), len(line)
            if n == 1:
                answer.append(line[0].ljust(maxWidth))
            else:
                #this is l not 1, very easy to misrecognize
                s, reminder = divmod(maxWidth-l, n-1)
                line[:-1] = [each+' '*s for each in line[:-1]]
                line[:reminder] = [each+' ' for each in line[:reminder]]
                answer.append(''.join(line))
            text = text[idx+1:]
        answer[-1] = ' '.join(answer[-1].split()).ljust(maxWidth)
        return answer
