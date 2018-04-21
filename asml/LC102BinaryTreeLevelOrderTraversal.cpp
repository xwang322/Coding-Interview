/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> answer;
        vector<int> sublist;
        queue<TreeNode*> q;
        if (!root) return answer;
        q.push(root);
        while (!q.empty()) {
            int count = q.size();
            for (int i = 0; i < count; i++) {
                if (q.front()->left) q.push(q.front()->left);
                if (q.front()->right) q.push(q.front()->right);
                sublist.push_back(q.front()->val);
                q.pop();
            }
            answer.push_back(sublist);
            sublist.clear();
        }
        return answer;
    }
};
