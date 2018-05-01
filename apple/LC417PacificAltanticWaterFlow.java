public class Solution {
    public List<int[]> pacificAtlantic(int[][] matrix) {
        List<int[]> answer = new LinkedList<>();
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return answer;
        int m = matrix.length;
        int n = matrix[0].length;
        boolean[][] pacific = new boolean[m][n];
        boolean[][] atlantic = new boolean[m][n];
        Queue<int[]> pa_q = new LinkedList<>();
        Queue<int[]> at_q = new LinkedList<>();
        for (int i = 0; i < m; i++) {
            pacific[i][0] = true;
            atlantic[i][n-1] = true;
            pa_q.offer(new int[]{i, 0});
            at_q.offer(new int[]{i, n-1});
        }
        for (int i = 0; i < n; i++) {
            pacific[0][i] = true;
            atlantic[m-1][i] = true;
            pa_q.offer(new int[]{0, i});
            at_q.offer(new int[]{m-1, i});
        }
        bfs(matrix, pacific, pa_q);
        bfs(matrix, atlantic, at_q);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    answer.add(new int[]{i, j});
                }
            }
        }
        return answer;
    }

    public void bfs(int[][] matrix, boolean[][] reached, Queue<int[]> queue) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] dirs = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        while (!queue.isEmpty()) {
            int[] node = queue.poll();
            for (int[] dir : dirs) {
                int x = node[0] + dir[0];
                int y = node[1] + dir[1];
                if (x<0 || x>=m || y<0 || y>=n || reached[x][y] || matrix[node[0]][node[1]]>matrix[x][y]) continue;
                reached[x][y] = true;
                queue.offer(new int[]{x, y});
            }
        }
    }
}
