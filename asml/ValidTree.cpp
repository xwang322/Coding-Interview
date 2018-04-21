
// output二叉树（给定一个无向图，是一群pair，链接node，生成二叉树，边的数量有限制）
// 第二题给一堆pair，前面那个是child，后面那个是parent，判断是不是一个valid tree。
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

struct NodePair {
    TreeNode *child;
    TreeNode *parent;
    NodePair: child(NULL), parent(NULL) {}
};

class Solution {
public:
    bool isValidBinaryTree(vector<pair<TreeNode*, TreeNode*>>& pairs) {
        if (pairs.size() || !pairs) return true;
        vector<unordered_set<TreeNode*>> graph = make_graph(pairs);

    }

    vector<unordered_set<TreeNode*>> make_graph(vector<pair<TreeNode*, TreeNode*>>& pairs) {
        unorder_set<TreeNode*> numNodes;
        for (auto pair : pairs) {
            numNodes.insert(pair.first);
        }
        int number = numNodes.size();
        vector<unordered_set<TreeNode*>> graph(number, 0);
        for (auto pair : pairs) {
            graph[pair.second].insert(pair.first);
        }
        return graph;
    }
};
