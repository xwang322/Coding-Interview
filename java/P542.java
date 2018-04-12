class Solution {
    public int M = Integer.MAX_VALUE;
    int[][] directions = {{1,0}, {-1,0}, {0,1}, {0,-1}};
    
    public int[][] updateMatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] answer = new int[m][n];
        Queue<int[]> q = new LinkedList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] != 0) answer[i][j] = M;
                else q.offer(getarray(i,j));
            }
        }
        
        int distance = 1;
        while (!q.isEmpty()) {
            Queue<int[]> next = new LinkedList<>();
            while (!q.isEmpty()) {
                int[] temp = q.poll();
                for (int[] d:directions) {
                    int first = d[0]+temp[0];
                    int second = d[1]+temp[1];
                    if (isValid(first, second, answer)) {
                        answer[first][second] = distance;
                        next.offer(getarray(first, second));
                    }
                }
            }
            distance++;
            q = next;
        }
        return answer;
        
    }
    
    public int[] getarray(int i, int j) {
        int[] A = new int[2];
        A[0] = i;
        A[1] = j;
        return A;
    }
    
    
    public boolean isValid(int first, int second, int[][]answer) {
        return first>=0 && first<answer.length && second>=0 && second<answer[0].length && answer[first][second] == M;
    }
}