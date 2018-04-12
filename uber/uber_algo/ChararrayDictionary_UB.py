/*
* list of words (dictionary) +
* array of characters -> return boolean contains(array, words) to check if a string in dict contains all chars in array.
* Test cases:
* // ['a', 'b', 'e'], "abes" -> True
* // ['a', 'b', 'c'], "abes" -> False
* // ['a', 'a'], "as" -> False
* // ['a', 'a'], "asaa" -> True
* 第一问很快写完，编译运行test cases通过。
* 然后 follow up: long list of words, return Shortest word in dictionary such that contains(array, word) is true.
* 面试官说完follow up还提示了下你可能需要对dict预处理。没想到什么太好的办法，一开始说是先对dict的words按长度排序，
* 这样在找string的时候长度少于array size的就可以直接忽略了，
* 面试官对这个好像不太满意，我又说可不可以把单词压缩下，这样占用空间就小了，这样一来好像之前的排序也没啥用了。。。
* 他不置可否，继续提问，你这个算法如果要scale要多个机器上，要做什么优化，我说能不能把字典分块，每个机器负责一部分工作，他说我不是要你做load balancing。。。
* 又瞎扯了一通，然后时间就差不多了，说你有什么问题要问我的，问完问题就结束了
* 周三收到通知说，由于这是个很短的面试（面试官迟到了十几分钟），代码写的不是太多（followup一直在讨论，没有写代码）所以要做第二轮店面。
**/
# first question is whether the chararray has to be the same order of occurance for each word in dictionary, the first one is not
import collections
def CharandDict(dictionary, chararray):
    if not dictionary:
        return []
    if not chararray:
        return dictionary
    answer = []
    char_counter = collections.Counter(chararray)
    for word in dictionary:
        flag = True
        temp_counter = collections.Counter(word)
        for key in char_counter:
            if key not in temp_counter or temp_counter[key] < char_counter[key]:
                flag = False
                break
        if flag:
            answer.append(word)
    return answer

answer = CharandDict(['abcced','see','abcb','eeadbc','eeeeee'], ['e'])
answer = CharandDict(['abcced','see','abcb','eeadbc','eeeeee'], ['a','b','c','e','s','f','c','s','a','d','e','e'])
print answer
# find the shortest assuming char array sequences has no influence
import collections
def CharandDictShortest(dictionary, chararray):
    if not dictionary:
        return []
    if not chararray:
        return dictionary
    answer = ''
    char_counter = collections.Counter(chararray)
    dictionary = sorted(dictionary, key=lambda x: len(x))
    if len(dictionary[-1]) < len(chararray):
        return ''
    for word in dictionary:
        if len(word) >= len(chararray):
            flag = True
            temp_counter = collections.Counter(word)
            for key in char_counter:
                if key not in temp_counter or temp_counter[key] < char_counter[key]:
                    flag = False
                    break
            if flag:
                answer = word
                break
    return answer

answer = CharandDictShortest(['abcced','see','abcb','eeadbc','eeeeee'], ['e'])
print answer
# if we consider the sequences of the char array matters, this will use DP to solve
import collections
def CharandDictDP(dictionary, chararray):
    if not dictionary:
        return []
    if not chararray:
        return dictionary
    answer = []
    for word in dictionary:
        word_list = list(word)
        word_list = iter(word_list)
        if all(char in word_list for char in chararray):
            answer.append(word)
    return answer

answer = CharandDictDP(['abcced','see','abcb','eeadbc','eeeeee'], ['a','b'])
print answer
# find the shortest assuming char array sequences has influence
import collections
def CharandDictShortestDP(dictionary, chararray):
    if not dictionary:
        return []
    if not chararray:
        return dictionary
    answer = ''
    dictionary = sorted(dictionary, key=lambda x: len(x))
    if len(dictionary[-1]) < len(chararray):
        return ''
    for word in dictionary:
        if len(word) >= len(chararray):
            word_list = list(word)
            word_list = iter(word_list)
            if all(char in word_list for char in chararray):
                answer = word
                break
    return answer

answer = CharandDictShortestDP(['abcced','see','abcb','eeadbc','eeeeee'], ['a','b'])
print answer
