class Solution {
public:
    vector<vector<int>> multiply(vector<vector<int>>& A, vector<vector<int>>& B) {
        if (A.empty() || B.empty()) return vector<vector<int>>();
        vector<vector<int>> answer(A.size(), vector<int>(B[0].size()));
        for (int i = 0; i < A.size(); i++) {
            for (int j = 0; j < B.size(); j++) {
                if (A[i][j] != 0) {
                    for (int k = 0; k < B[0].size(); k++) {
                        answer[i][k] += A[i][j]*B[j][k];
                    }
                }
            }
        }
        return answer;
    }
};
