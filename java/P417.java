class Solution {
    // dfs
    int[][] dir = new int[][]{{0,1}, {0,-1}, {1,0}, {-1,0}};
    public List<int[]> pacificAtlantic(int[][] matrix) {
        List<int[]> answer = new LinkedList<>();
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return answer;
        }
        int n = matrix.length,  m = matrix[0].length;
        boolean[][] pacific = new boolean[n][m];
        boolean[][] altantic = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            dfs(matrix, pacific, Integer.MIN_VALUE, i, 0);
            dfs(matrix, altantic, Integer.MIN_VALUE, i, m-1);
        }
        for (int i = 0; i < m; i++) {
            dfs(matrix, pacific, Integer.MIN_VALUE, 0, i);
            dfs(matrix, altantic, Integer.MIN_VALUE, n-1, i);
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (pacific[i][j] && altantic[i][j]) {
                    answer.add(new int[] {i,j});
                }
            }
        }
        return answer;  
    }
    
    private void dfs(int[][] matrix, boolean[][] visited, int height, int x, int y) {
        int n = matrix.length, m = matrix[0].length;
        if (x<0 || y<0 || y>=m || x>=n || visited[x][y] || matrix[x][y] < height) 
            return;
        visited[x][y] = true;
        for (int[]d:dir) {
            dfs(matrix, visited, matrix[x][y], x+d[0], y+d[1]);
        }
    }
}