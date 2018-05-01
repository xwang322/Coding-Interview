//单词查找那道hard(一个印度manager出的，打出来之后，明显态度翻转了)
class Solution {
    class TrieNode {
        TrieNode[] next = new TrieNode[26];
        String word;
    }
    public TrieNode buildtrie(String[] words) {
        TrieNode root = new TrieNode();
        for (String word : words) {
            TrieNode t = root;
            for (char c : word.toCharArray()) {
                int temp = c - 'a';
                if (t.next[temp] == null) t.next[temp] = new TrieNode();
                t = t.next[temp];
            }
            t.word = word;
        }
        return root;
    }

    public List<String> findWords(char[][] board, String[] words) {
        List<String> answer = new ArrayList<>();
        TrieNode root = buildtrie(words);
        int m = board.length;
        int n = board[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dfs(board, m, n, i, j, root, answer);
            }
        }
        return answer;
    }

    public void dfs(char[][] board, int m, int n, int i, int j, TrieNode root, List<String> answer) {
        if (i < 0 || i >= m || j < 0 || j >= n) return;
        char c = board[i][j];
        if (c == '#' || root.next[c-'a'] == null) return;
        root = root.next[c-'a'];
        if (root.word != null) {
            answer.add(root.word);
            root.word = null;
        }
        board[i][j] = '#';
        dfs(board, m, n, i+1, j, root, answer);
        dfs(board, m, n, i-1, j, root, answer);
        dfs(board, m, n, i, j+1, root, answer);
        dfs(board, m, n, i, j-1, root, answer);
        board[i][j] = c;
    }
}
