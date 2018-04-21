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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        if (!root) return {};
        vector<vector<int>> answer;
        vector<int> sublist;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            int count = q.size();
            for (int i = 0; i < count; i++) {
                if (q.front()->left != NULL) q.push(q.front()->left);
                if (q.front()->right != NULL) q.push(q.front()->right);
                sublist.push_back(q.front()->val);
                q.pop();
            }
            answer.insert(answer.begin(), sublist);
            sublist.clear();
        }
        return answer;
    }
};
