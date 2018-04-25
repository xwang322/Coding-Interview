// output二叉树（给定一个无向图，是一群pair，链接node，生成二叉树，边的数量有限制）
#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_set>
#include <unordered_map>
using namespace std;
struct TreeNode {
    int val;
    TreeNode(int x) : val(x) {}
};

struct NodePair {
    TreeNode* child;
    TreeNode* parent;
    NodePair(TreeNode* c, TreeNode* p) {
      child = c;
      parent = p;
    }
};

unordered_map<TreeNode* , unordered_set<TreeNode*>> make_graph(int number, vector<NodePair*>& pairs) {
    unordered_map<TreeNode*, unordered_set<TreeNode*>> graph;
    for (auto pair : pairs) {
        graph[pair->child].insert(pair->parent);
        // cout << pair->parent->val << " " << pair->child->val << endl;
    }
    // cout << graph.size() << endl;
    return graph;
}

bool isValidBinaryTree(vector<NodePair*>& pairs) {
    if (pairs.size()==0) return true;
    unordered_set<TreeNode*> numNodes;
    for (auto pair : pairs) {
        numNodes.insert(pair->child);
        numNodes.insert(pair->parent);
    }
    int number = numNodes.size();
    unordered_map<TreeNode*, unordered_set<TreeNode*>> graph = make_graph(number, pairs);
    int degreezero = 0;
    for (auto node : numNodes) {
        if (graph[node].size() == 0) {
            degreezero++;
        }
    }
    // cout << degreezero << endl;
    if (degreezero == 0) return false;
    else if (degreezero > 1) return false;
    return true;
}


int main(int argc, char* argv[]) {
    TreeNode * n1 = new TreeNode(1);
    TreeNode * n2 = new TreeNode(2);
    TreeNode * n3 = new TreeNode(3);
    NodePair* np1 = new NodePair(n1, n2);
    NodePair* np2 = new NodePair(n2, n3);
    NodePair* np3 = new NodePair(n3, n1);
    vector<NodePair*> pairs{np1, np2, np3};
    bool answer = isValidBinaryTree(pairs);
    cout << answer << endl;
}
