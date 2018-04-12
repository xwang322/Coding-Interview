/*
* 第一轮：Coding，国人大哥 给一个二维 board （4 * 4） 和 一个 list of words.对于board, 每一个元素是一个字母。
* 可以通过这些字母连线组成单词，连线可以为左，右，上，下，左上，右上，左下，右下，移动一位，共八种移动方式，但board 里已用过的元素不能再次使用。
* 单词长度不定。问list 中的每一个单词是否能够通过 board 里的字母连线组成。楼主一开始用的是 DFS，写完。
* 小哥问如果 words 很多的话，怎么改进。答可以用 Trie. 把 board 里面的所有可能单词都放进 Trie, 然后可以看 list 的每一个单词是否在 Trie 中。
* ImplementTrie.完。
**/
def WordSearchMutation(board, words):
    if not board or not words:
        return []
    trie = {}
    temp = []
    for word in words:
        t = trie
        for char in word:
            if char not in t:
                t[char] = {}
            t = t[char]
        t['#'] = '#'
    m = len(board)
    n = len(board[0])
    for i in range(m):
        for j in range(n):
            dfs(board, temp, i, j, m, n, trie, '')
    answer = []
    for each in temp:
        if each not in answer:
            answer.append(each)
    return answer

def dfs(board, temp, i, j, m, n, trie, path):
    if '#' in trie:
        temp.append(path)
    if i < 0 or i >= m or j < 0 or j >= n:
        return
    if board[i][j] in trie:
        char = board[i][j]
        board[i][j] = '*'
        dfs(board, temp, i+1, j, m, n, trie[char], path+char)
        dfs(board, temp, i-1, j, m, n, trie[char], path+char)
        dfs(board, temp, i, j+1, m, n, trie[char], path+char)
        dfs(board, temp, i, j-1, m, n, trie[char], path+char)
        dfs(board, temp, i+1, j+1, m, n, trie[char], path+char)
        dfs(board, temp, i+1, j-1, m, n, trie[char], path+char)
        dfs(board, temp, i-1, j+1, m, n, trie[char], path+char)
        dfs(board, temp, i-1, j-1, m, n, trie[char], path+char)
        board[i][j] = char


answer = WordSearchMutation([["o","a","i","n"],["e","t","a","e"],["p","h","k","r"],["i","f","l","v"]],
["oath","pea","eat","rain"])
print answer
