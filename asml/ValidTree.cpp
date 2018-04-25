// 第二题给一堆pair，前面那个是child，后面那个是parent，判断是不是一个valid tree。
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
    TreeNode *child;
    TreeNode *parent;
    NodePair(TreeNode* c, TreeNode* p) {
        child = c;
        parent = p;
    }
};

unordered_map<TreeNode*, unordered_set<TreeNode*>> make_graph(int number, vector<NodePair*>& pairs) {
    unordered_map<TreeNode*, unordered_set<TreeNode*>> graph;
    //unordered_map<TreeNode*, <unordered_set<TreeNode*>>()
    for (auto pair : pairs) {
        graph[pair->child].insert(pair->parent);
        //cout << pair->child->val << " " << pair->parent->val << endl;
    }
    return graph;
}

bool isValidBinaryTree(vector<NodePair*>& pairs) {
    if (pairs.size()==0) return true;
    unordered_set<TreeNode*> numNodes;
    for (auto pair : pairs) {
        numNodes.insert(pair->child);
        numNodes.insert(pair->parent);
        //cout << pair->child->val << endl;
    }
    int number = numNodes.size();
    unordered_map<TreeNode*, unordered_set<TreeNode* >> graph = make_graph(number, pairs);
    int degreezero = 0;
    for (auto node : numNodes) {
        if (graph[node].size() == 0) degreezero++;
    }
    if (degreezero == 0) return false;
    else if (degreezero > 1) return false;
    return true;
}

int main(int argc, char* argv[]) {
    TreeNode* node1 = new TreeNode(1);
    TreeNode* node2 = new TreeNode(2);
    TreeNode* node3 = new TreeNode(3);
    NodePair* p1 = new NodePair(node1, node2);
    NodePair* p2 = new NodePair(node2, node3);
    NodePair* p3 = new NodePair(node3, node1);
    vector<NodePair*> input{p1, p2, p3};
    bool answer = isValidBinaryTree(input);
    cout << answer << endl;
}
