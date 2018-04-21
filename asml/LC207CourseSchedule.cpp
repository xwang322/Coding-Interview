class Solution {
public:
    bool canFinish(int numCourses, vector<pair<int, int>>& prerequisites) {
        vector<unordered_set<int>> graph = make_graph(numCourses, prerequisites);
        vector<int> degrees = compute_degree(graph);
        for (int i = 0; i < numCourses; i++) {
            int j = 0;
            for (; j < numCourses; j++) {
                if (!degrees[j]) break;
            }
            if (j == numCourses) return false;
            degrees[j] = -1;
            for (auto neighbor : graph[j]) {
                degrees[neighbor]--;
            }
        }
        return true;
    }

    vector<unordered_set<int>> make_graph(int numCourses, vector<pair<int, int>>& prerequisites) {
        vector<unordered_set<int>> graph(numCourses);
        for (auto prerequisite : prerequisites) {
            graph[prerequisite.second].insert(prerequisite.first);
        }
        return graph;
    }

    vector<int> compute_degree(vector<unordered_set<int>>& graph) {
        vector<int> degrees(graph.size(), 0);
        for (auto edge: graph) {
            for (auto neighbor : edge) {
                degrees[neighbor]++;
            }
        }
        return degrees;
    }
};
