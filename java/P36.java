class Solution {
    public boolean isValidSudoku(char[][] board) {
        if (board == null || board.length == 0) return false;
        for (int i = 0; i < 9; i++) {
            HashSet<Character> row = new HashSet<Character>();
            HashSet<Character> col = new HashSet<Character>();
            HashSet<Character> square = new HashSet<Character>();
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.' && !row.add(board[i][j])) return false;
                if (board[j][i] != '.' && !col.add(board[j][i])) return false;
                int rowindex = 3*(i/3);
                int colindex = 3*(i%3);
                if (board[rowindex+j/3][colindex+j%3] != '.' && !square.add(board[rowindex+j/3][colindex+j%3])) return false;
            }
        }
        return true;
    }
}