/*
* 给出一个List<String>,代表一个字典
* 问题1：返回该字典里所有的回文串(palindrome)，这个比较简单，没什么难度。随便秒
* 问题2：follow up， 返回字典里所有的pair，这个pair加一起可以组合成一个回文串
* 例子，比如字典里有{"race", "car"}
* “race”这个词本身不是回文串
* "car"这个词本身也不是回文串
* 但如果加一起就成了"racecar"，这就是回文串
* 问题3：follow up，如果碰到这样的特殊情况怎么办（也就是词语本身不是回文串，但是该单词的开头或者结尾是回文串）
* “xyxaaaa”和"aaaa"
* 再比如"a1axxyyxx",“a1a这种情况” 再比如,"xyxaaa"和“xyx”, "axyx", "aaxyx", "aaaxyx", "aaa"都可以是合法的pair
**/

def PalindromeCombo(strings):
    if not strings:
        return []
    answer1 = []
    for string in strings:
        if string == string[::-1]:
            answer1.append(string)
    answer2 = []
    for string in strings:
        for another in strings:
            if string != another:
                if string+another == another[::-1]+string[::-1]:
                    if (string, another) not in answer2:
                        answer2.append((string,another))
    answer3 = []
    for string in strings:
        for another in strings:
            if string != another:
                if string.startswith(another) or string[::-1].startswith(another):
                    if (string, another) not in answer3:
                        answer3.append((string, another))
    return answer1, answer2, answer3

answer = PalindromeCombo(['aaa','xyx','axyx','aaxyx','aaaxyx','xyxaaa','aaaa','xyxaaaa','a1a','a1axxyyxx'])[2]
print answer
              
