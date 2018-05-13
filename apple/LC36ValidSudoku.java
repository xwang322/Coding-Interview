class Solution {
    public boolean isValidSudoku(char[][] board) {
        if (board == null || board.length == 0 || board[0].length == 0) return false;
        return (checkRow(board) && checkCol(board) && checkDiag(board));
    }

    public boolean checkRow(char[][] board) {
        for (int i = 0; i < 9; i++) {
            Set<Character> set = new HashSet<>();
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    if (!set.add(board[i][j])) return false;
                    set.add(board[i][j]);
                }
            }
        }
        return true;
    }

    public boolean checkCol(char[][] board) {
        for(int i = 0; i < 9; i++) {
            Set<Character> set = new HashSet<>();
            for (int j = 0; j < 9; j++) {
                if (board[j][i] != '.') {
                    if (!set.add(board[j][i])) return false;
                    set.add(board[j][i]);
                }
            }
        }
        return true;
    }

    public boolean checkDiag(char[][] board) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                Set<Character> set = new HashSet<>();
                for (int i1 = 3*i; i1 < 3*i+3; i1++) {
                    for (int j1 = 3*j; j1 < 3*j+3; j1++) {
                        if (board[i1][j1] != '.') {
                            if (!set.add(board[i1][j1])) return false;
                            set.add(board[i1][j1]);
                        }
                    }
                }
            }
        }
        return true;
    }
}
