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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (preorder.size() == 0 or inorder.size() == 0) return NULL;
        return helper(preorder, 0, preorder.size(), inorder, 0, inorder.size());
    }

    TreeNode* helper(vector<int>& preorder, int i1, int j1, vector<int>& inorder, int i2, int j2) {
        if (i1>=j1 || i2>=j2) return NULL;
        int mid = preorder[i1];
        auto f = find(inorder.begin() + i2, inorder.begin() + j2, mid);
        int dis = f - inorder.begin() - i2;
        TreeNode* root = new TreeNode(mid);
        root->left = helper(preorder, i1+1, i1+1+dis, inorder, i2, i2+dis);
        root->right = helper(preorder, i1+1+dis, j1, inorder, i2+1+dis, j2);
        return root;
    }
};
