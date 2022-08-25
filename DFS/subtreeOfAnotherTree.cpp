/**
 0572 Subtree of Another Tree
 There are advanced solutions,
 I decide to go with DFS. 
 */
class Solution {
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) 
    {
        if (root == nullptr) 
        {
            return false;
        }
        return checkIt(root, subRoot) || isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }
    bool checkIt(TreeNode* root, TreeNode* subRoot) 
    {
        if (root == nullptr && subRoot == nullptr) 
        {
            return true;
        }
        else if (root == nullptr || subRoot == nullptr) 
        {
            return false;
        }
        else if (root->val == subRoot->val) 
        {
            return checkIt(root->left, subRoot->left) && checkIt(root->right, subRoot->right);
        }
        else 
        {
            return false;
        }
    }
};