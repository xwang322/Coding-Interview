class Solution {
    public String alienOrder(String[] words) {
        boolean[][] level = new boolean[26][26];
        int[] visited = new int[26];
        buildGraph(visited, words, level);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 26; i++) {
            if (visited[i] == 0) {
                if (!dfs(level, visited, sb, i)) return "";
            }
        }
        return sb.reverse().toString();
    }

    public boolean dfs(boolean[][] level, int[] visited, StringBuilder sb, int i) {
        visited[i] = 1;
        for (int j = 0; j < 26; j++) {
            if (level[i][j]) {
                if (visited[j] == 1) return false;
                if (visited[j] == 0) {
                    if (!dfs(level, visited, sb, j)) return false;
                }
            }
        }
        visited[i] = 2;
        sb.append((char)(i+'a'));
        return true;
    }

    public void buildGraph(int[] visited, String[] words, boolean[][] level) {
        Arrays.fill(visited, -1);
        for (int i = 0; i < words.length; i++) {
            for (Character c :  words[i].toCharArray()) {
                visited[c-'a'] = 0;
            }
            if (i > 0) {
                String w1 = words[i-1], w2 = words[i];
                for (int j = 0; j < Math.min(w1.length(), w2.length()); j++) {
                    if (w1.charAt(j) != w2.charAt(j)) {
                        level[w1.charAt(j) - 'a'][w2.charAt(j) - 'a'] = true;
                        break;
                    }
                }
            }
        }
    }
}
