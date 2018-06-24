#include <iostream>
using namespace std;
struct TreeNode
{
		int val;
		TreeNode * left;
		TreeNode * right;
		TreeNode(int x):val(x), left(NULL), right(NULL){}
	
};
class solution{
public:
	TreeNode * insert(TreeNode* root, int val)
	{
		if(!root)return new TreeNode(val);
		TreeNode * temp=root;
		while(temp)
		{
			if(val < temp->val){
				if(temp->left)temp=temp->left;
				else{
					temp->left=new TreeNode(val);
					return root;
				}
			}
			else {
				if(temp->right)temp=temp->right;
				else{
					temp->right=new TreeNode(val);
					return root;
				}
			}
		}

		return root;

	}
	TreeNode * getmin(TreeNode * node)
	{
		if(!node)return NULL;
         while(node->left)
         {
             node=node->left;
         }
         return node;
	}
	 TreeNode* removeNode(TreeNode* root, int val) {
        
        if(!root)return root;
        if(val < root->val)root->left=removeNode(root->left, val);
        else if(val > root->val)root->right=removeNode(root->right, val);
        
        else {
            if (root->left == NULL)
            {
                TreeNode *temp = root->right;
                free(root);
                return temp;
             }
            else if (root->right == NULL)
            {
            TreeNode *temp = root->left;
            free(root);
            return temp;
            }
            
            TreeNode* temp=getmin(root->right);
            root->val=temp->val;
            root->right = removeNode(root->right, temp->val);
        }
        return root;
        
    }

    void printTree(TreeNode * root)
    {
    	if(!root)return;
    	printTree(root->left);
    	cout << root->val << endl;
    	printTree(root->right);
    }

};
int main()
{
	TreeNode * root=NULL;
	solution s;
	root=s.insert(root, 10);
	root=s.insert(root, 6);
	root=s.insert(root, 13);
	root=s.insert(root, 4);
	root=s.insert(root, 12);
	root=s.removeNode(root, 4);
	s.printTree(root);


	return 0;
}