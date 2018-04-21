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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (!root) return {};
        vector<vector<int>> answer;
        stack<TreeNode*> this_layer;
        this_layer.push(root);
        vector<int> value_layer;
        bool flag = true;
        while (!this_layer.empty()) {
            int count = this_layer.size();
            stack<TreeNode*> next_layer;
            for (int i = 0; i < count; i++) {
                TreeNode* node = this_layer.top();
                this_layer.pop();
                value_layer.push_back(node->val);
                if (flag) {
                    if (node->left) next_layer.push(node->left);
                    if (node->right) next_layer.push(node->right);
                } else {
                    if (node->right) next_layer.push(node->right);
                    if (node->left) next_layer.push(node->left);
                }

            }
            answer.push_back(value_layer);
            flag = !flag;
            this_layer = next_layer;
            value_layer.clear();
        }
        return answer;
    }
};
