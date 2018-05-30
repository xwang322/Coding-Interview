class Solution(object):
    def fullJustify(self, words, maxWidth):
        wordtext = ' '.join(words) + ' '
        if wordtext == ' ':
            return [' '*maxWidth]
        answer = []
        while wordtext:
            breakpoint = wordtext.rfind(' ', 0, maxWidth+1)
            # maxWidth+1 easy to forget+1
            contents = wordtext[:breakpoint].split()
            totalnumber = len(contents)
            totallength = sum(len(content) for content in contents)
            if totalnumber == 1:
                answer.append(contents[0].ljust(maxWidth))
            else:
                numbergap, restgap = divmod(maxWidth - totallength, totalnumber-1)
                contents[:-1] = [each + ' '*numbergap for each in contents[:-1]]
                contents[:restgap] = [each + ' ' for each in contents[:restgap]]
                answer.append(''.join(contents))
            wordtext = wordtext[breakpoint+1:]
        answer[-1] = ' '.join(answer[-1].split()).ljust(maxWidth)
        return answer
                
