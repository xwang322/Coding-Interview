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
    bool isValidBST(TreeNode* root) {
        return dfs(root, NULL, NULL);
    }

    bool dfs(TreeNode* root, TreeNode* minimum, TreeNode* maximum) {
        if (root == NULL) return true;
        if (minimum != NULL && root->val <= minimum->val) return false;
        if (maximum != NULL && root->val >= maximum->val) return false;
        return dfs(root->left, minimum, root) && dfs(root->right, root, maximum);
    }
};
