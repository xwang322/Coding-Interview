class Solution {
    public int maximalSquare(char[][] matrix) {
        if (matrix.length == 0) return 0;
        int m = matrix.length, n = matrix[0].length, result = 0;
        int[][] temp = new int[m+1][n+1];
        for (int i = 1; i < m+1; i++) {
            for (int j = 1; j < n+1; j++) {
                if (matrix[i-1][j-1] == '1') {
                    temp[i][j] = Math.min(Math.min(temp[i-1][j-1], temp[i-1][j]), temp[i][j-1])+1;
                    result = Math.max(temp[i][j], result);
                }
            }
        }
        return result*result;
    }
}