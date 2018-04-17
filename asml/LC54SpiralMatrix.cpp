class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if (matrix.size() == 0 || matrix[0].size() == 0) return {};
        int row_up = 0;
        int row_down = matrix.size()-1;
        int col_up = 0;
        int col_down = matrix[0].size()-1;
        int k = 0;
        vector<int> answer(matrix.size()*matrix[0].size());
        while ((row_up <= row_down) && (col_up <= col_down)) {
            int i = col_up;
            while (i <= col_down) {
                answer[k++] = matrix[row_up][i];
                i++;
            }
            row_up++;
            i = row_up;
            while (i <= row_down) {
                answer[k++] = matrix[i][col_down];
                i++;
            }
            col_down--;
            if (row_up <= row_down) {
                i = col_down;
                while (i >= col_up) {
                    answer[k++] = matrix[row_down][i];
                    i--;
                }
                row_down--;
            }
            if (col_up <= col_down) {
                i = row_down;
                while (i >= row_up) {
                    answer[k++] = matrix[i][col_up];
                    i--;
                }
                col_up++;
            }
        }
        return answer;
    }
};
