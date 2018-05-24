'''
昨天做了EA第二轮面试，题目是parse assembly lauguage string, 然后判断对应的16个寄存器的位置，给定一些操作，比如set, mov, jmp, jz, and, or 让你实现，经过一系列instructinos之后，对应的寄存器的值是什么，
如果陷入了死循环，就打印"HANGS!"，每个程序都会用"STOP"进行结尾。有的时候"STOP"会在中间给出（这种情况意味着这段程序可能有多个stop）。
具体的例子：
Program #0:
SET 0 1
NOT 2
MOV 4 2
AND 4 0
OR 6 4
STOP
Output:
0 0 0 0 0 0 0 0 0 1 0 1 0 1 0 1
Explanation:
This is a sequential program with no jumps. Note in the output the right-most bit is REG[0],
left-most is REG[15].
'''
def parseAssembleLang(strings):
    answer = [0 for i in range(16)]
    if not strings:
        return answer
    visited = set()
    dictionary_jmp = {}
    dictionary_jz = {}
    zf = False
    last_jmp = [0 for i in range(16)]
	i = 0
    while i < len(strings):
		string = strings[i]
        parseString = string.split()
        if len(parseString) == 2 and parseString[0] != 'NOT':
            if parseString[0] == 'JMP':
				if parseString[1] in dictionary_jmp and dictionary_jmp[parseString[1]] == answer:
					print "HANGS"
					break
				else:
					dictionary_jmp[parseString[1]] = answer
					i = parseString[1] - 1
            elif parseString[0] == 'JZ':
                if last[0] == 'CMP':
                    zf = (last[1] == last[2])
                elif last[0] == 'TEST':
                    zf = (last[1] and last[2])
                if zf:
                    if parseString[1] in dictionary_jz and dictionary_jz[parseString[1]] == answer:
						print "HANGS"
						break
					else:
						dictionary_jz[parseString[1]] = answer
						i = parseString[1] - 1
        elif len(parseString) == 2 and parseString[0] == 'NOT':
            answer[int(parseString[1])] = int(not answer[int(parseString[1])])
        elif len(parseString) == 3:
            if parseString[0] == 'AND':
                answer[int(parseString[1])]  = answer[int(parseString[1])] and answer[int(parseString[2])]
            elif parseString[0] == 'OR':
                answer[int(parseString[1])]  = answer[int(parseString[1])] or answer[int(parseString[2])]
            elif parseString[0] == 'SET':
                answer[int(parseString[1])]  = int(parseString[2])
            elif parseString[0] == 'MOV':
                answer[int(parseString[1])]  = answer[int(parseString[2])]
        elif len(parseString) == 1 and parseString[0] == 'STOP':
            return answer[::-1]
        last = parseString
		i += 1
    return answer[::-1]

answer = parseAssembleLang(['SET 0 1', 'NOT 2','MOV 4 2' ,'AND 4 0' ,'OR 6 4' ,'STOP'])
print answer
