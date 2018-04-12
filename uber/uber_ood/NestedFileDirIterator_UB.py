/*
* 优步的电面 是一个实现一个file 的 iterator 实现按string 的iteration
* input path: file/directory, each directory can contain more files or directory. Each file is txt.
* dirA
*     -- dirB
*         -- fileB"hello world"
*         -- directory C
*             -- fileC"hello "
*             -- fileD"world"
*     -- fileA"kitty"
* output: an interator class,
* [hello world hello world kitty].
* public class WordIterator implements Iterator {
*       hasNext()
*       Next()
* }
* 注意要实现按string 的iterator 楼主一开始实现按 file 的结果被面试官说要2步iterator 要先按file再按string
* 估计挂了
**/
# my guess for the input is based on LC388: 'dirA\n\tdirB\n\t\tfileB.txt"hello world"\n\t\tdirC\n\t\t\tfileC.txt"hello"\n\t\t\tfileD.txt"world"\n\tfileA.txt"kitty"\n'
class NestedString(object):
    def __init__(self, nestedString):
        self.nestedString = nestedString
        self.answer = []
        while self.hasNext():
            temp = self.nestedString[:self.nestedString.find('\n')]
            if '.txt' in temp:
                start = temp.find('\"')+1
                end = temp.find('\"', start)
                self.answer.append(temp[start:end])
            self.nestedString = self.next()
        #print self.answer

    def next(self):
        return self.nestedString[self.nestedString.find('\n')+1:]

    def hasNext(self):
        return not self.nestedString == ''


NestedString('dirA\n\tdirB\n\t\tfileB.txt"hello world"\n\t\tdirC\n\t\t\tfileC.txt"hello"\n\t\t\tfileD.txt"world"\n\tfileA.txt"kitty"\n')
