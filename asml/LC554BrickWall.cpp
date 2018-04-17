class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        if (wall.empty()) return 0;
        unordered_map<int, int> dictionary;
        int row = wall.size();
        int minimum = 0;
        for (int i = 0; i < row; i++) {
            int length = 0;
            for (int j = 0; j < wall[i].size()-1; j++) {
                length += wall[i][j];
                dictionary[length]--;
                minimum = min(minimum, dictionary[length]);
            }
        }
        return row+minimum;
    }
};
