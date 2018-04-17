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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        if (postorder.size() == 0 || inorder.size() == 0) return NULL;
        return helper(inorder, 0, inorder.size(), postorder, 0, postorder.size());
    }
    TreeNode* helper(vector<int>& inorder, int i1, int j1, vector<int>& postorder, int i2, int j2) {
        if (i1 >= j1 || i2 >= j2) return NULL;
        int mid = postorder[j2-1];
        auto f = find(inorder.begin()+i1, inorder.begin()+j1, mid);
        int dis = f-inorder.begin()-i1;
        TreeNode* root = new TreeNode(mid);
        root->left = helper(inorder, i1, i1+dis, postorder, i2, i2+dis);
        root->right = helper(inorder, i1+dis+1, j1, postorder, i2+dis, j2-1);
        return root;
    }
};
