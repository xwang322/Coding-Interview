class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        if (n == 0) return {};
        vector<vector<int>> answer(n, vector<int>(n));
        int row_up = 0;
        int row_down = n-1;
        int col_up = 0;
        int col_down = n-1;
        int count = 1;
        while (row_up <= row_down && col_up <= col_down) {
            for (int i = col_up; i < col_down+1; i++) {
                answer[row_up][i] = count;
                count++;
            }
            row_up++;
            for (int i = row_up; i < row_down+1; i++) {
                answer[i][col_down] = count;
                count++;
            }
            col_down--;
            if (row_up <= row_down){
                for (int i = col_down; i > col_up-1; i--) {
                    answer[row_down][i] = count;
                    count++;
                }
                row_down--;
            }
            if (col_up <= col_down) {
                for (int i = row_down; i > row_up-1; i--) {
                    answer[i][col_up] = count;
                    count++;
                }
                col_up++;
            }
        }
        return answer;
    }
};
