/*
* 电面45分钟, 题目是 breaking bad + 分析时间空间复杂度。有点赶，但总算是有写完。
* Given an array of strings `words` and a string `name`, find one substring of `name` that matches any word in `words`.
* Put brackets around the matching substring in `name` and capitalize the first letter.
* Sample input: words = ['B', 'Ar', 'O']
* name = 'aaron'
* Output:  a[Ar]on
* Followup. Find all possible ways of breaking bad.
* Sample input:
* words = ['B', 'Ar', 'O']
* name = 'aaron
* Output:['a[Ar][O]n', 'aaron', 'a[Ar]on', 'aar[O]n']
**/

def breakingbad(words, string):
    if not words or not string:
        return string
    for word in words:
        for i in range(len(string)):
            if string[i:].startswith(word.lower()):
                return string[:i]+word+string[i+len(word):]
    return string

def breakingbad_followup(words, string):
    answer = []
    answer.append(string)
    for word in words:
        for i in range(len(string)):
            if string[i:].startswith(word.lower()):
                temp = string[:i]+word+string[i+len(word):]
                answer.append(temp)
                temp_answer = breakingbad_followup(words, temp)
                for each in temp_answer:
                    if each not in answer:
                        answer.append(each)
    return answer

answer = breakingbad_followup(['B', 'Ar', 'O','N'], 'aaron')
print answer
