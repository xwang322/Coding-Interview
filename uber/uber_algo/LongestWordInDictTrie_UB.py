/*
* 应该是某个游戏，忘记叫啥了。给英文字典，和字符数组。问最长可以拼出来的单词。
* 写了最傻的字符数组排列组合。中间讨论了复杂度讨论了很久。
* 这题复杂度给了N^N,不知道对不对。也有可能讨论复杂度是要我找另外解法。听口气是要便利字典检查从最长到最短的。中间提到过这个办法面试官也没说什么。
* 中间还问机子要几秒能跑完10个字符...有可能是想说这个解法慢吧，我还瞎算半天
* 没有运行，因为他说给的是全英文字典，这个看样子就是跑不了了。
**/

# potentail useful link: https://www.geeksforgeeks.org/find-the-k-most-frequent-words-from-a-file/
# simple solution does not matter the chronological order, as long as the len is the maximum
import collections
def findlongestWord(dictionary, chararray):
    if not dictionary or not chararray:
        return ''
    counter_char_array = collections.Counter(chararray)
    dictionary = sorted(dictionary, key=lambda x:len(x))
    print dictionary
    answer = ''
    for i in range(len(dictionary)-1, -1, -1):
        flag = True
        temp_dict = collections.Counter(dictionary[i])
        for key in temp_dict:
            if key not in counter_char_array or temp_dict[key] > counter_char_array[key]:
                flag = False
                break
        if flag:
            answer = dictionary[i]
            break
    return answer
# if needs to ouput the same length but minimum chronological order
import collections
def findlongestWord(dictionary, chararray):
    if not dictionary or not chararray:
        return ''
    counter_char_array = collections.Counter(chararray)
    dictionary = sorted(dictionary, key=lambda x:len(x))
    answer = 'z'*(len(dictionary[-1]))
    for i in range(len(dictionary)-1, -1, -1):
        flag = True
        temp_dict = collections.Counter(dictionary[i])
        for key in temp_dict:
            if key not in counter_char_array or temp_dict[key] > counter_char_array[key]:
                flag = False
                break
        # if needs to ouput the same length but minimum chronological order
        if flag:
            if len(answer) == len(dictionary[i]) and dictionary[i] < answer:
                answer = dictionary[i]
                break
    return answer if answer != 'z'*(len(dictionary[-1])) else ''

answer = findlongestWord(['abcced','see','abcb','eeadbc','eeeeee'], ['a','b','c','e','s','f','c','s','a','d','e','e'])
print answer

# try to use Trie to solve this problem. This returns the longest word but not minimum chronological order
def findlongestWordByTrie(dictionary, chararray):
    if not dictionary or not chararray:
        return ''
    trie = {}
    dictionary = sorted(dictionary, key=lambda x:len(x))
    for word in dictionary:
        t = trie
        for char in word:
            if char not in t:
                t[char] = {}
            t = t[char]
        t['#'] = '#'
    answer = []
    dfs(answer, trie, chararray, '')
    return sorted(answer, key=lambda x:len(x))[-1]

def dfs(answer, trie, chararray, path):
    if '#' in trie:
        answer.append(path)
        return
    for char in trie:
        if char in chararray:
            chararray.remove(char)
            dfs(answer, trie[char], chararray, path+char)
            chararray.append(char)

answer = findlongestWordByTrie(['abcced','see','abcb','eeadbc','eeeeee'], ['a','b','c','e','s','f','c','s','a','d','e','e'])
print answer
