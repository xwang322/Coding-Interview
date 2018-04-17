class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c) {
        int m = nums.size();
        int n = nums[0].size();
        int product = m*n;
        if (r*c != product) return nums;
        vector<vector<int>> answer(r, vector<int>(c, 0));
        for (int i = 0; i < product; i++) {
            answer[i/c][i%c] = nums[i/n][i%n];
        }
        return answer;
    }
};
