class Solution {
public:
    int trapRainWater(vector<vector<int>>& heightMap) {
        if (heightMap.size() == 0 || heightMap[0].size() == 0) return 0;
        int m = heightMap.size();
        int n = heightMap[0].size();
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        vector<vector<int>> visited(m, vector<int>(n, 0));
        int answer = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 || j == 0 || i == m-1 || j == n-1) {
                    pq.push(make_pair(heightMap[i][j], n*i+j));
                    visited[i][j] = 1;
                }
            }
        }
        vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
        while (!pq.empty()) {
            auto val = pq.top(); pq.pop();
            int height = val.first;
            int x = val.second/n;
            int y = val.second%n;
            for (auto d:directions) {
                int x2 = x+d[0];
                int y2 = y+d[1];
                if (x2 >= m || x2 < 0 || y2 >= n || y2 < 0 || visited[x2][y2]) continue;
                visited[x2][y2] = 1;
                if (heightMap[x2][y2] < height) {
                    answer += height - heightMap[x2][y2];
                    pq.push(make_pair(height, x2*n+y2));
                } else {
                    pq.push(make_pair(heightMap[x2][y2], x2*n+y2));
                }
            }
        }
        return answer;
    }
};
