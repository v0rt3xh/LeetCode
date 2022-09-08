/**
 * 0110 Balanced Binary Tree
 Top-down
 Bottom-up
 Recursion
 */
class Solution1 
{
public:
    int getHeight(TreeNode* node) 
    {
        if (node == nullptr) 
        {
            return 0;
        }
        return max(getHeight(node->left), getHeight(node->right)) + 1;
    }
    
    bool isBalanced(TreeNode* root) 
    {
        if (root == nullptr) 
        {
            return true;
        }
        return abs(getHeight(root->left) - getHeight(root->right)) <= 1 && isBalanced(root->left) && isBalanced(root->right);
    }
};

class Solution2 
{
public:
    int getHeight(TreeNode* node) 
    {
        if (node == nullptr) 
        {
            return 0;
        }
        int leftHeight = getHeight(node->left);
        int rightHeight = getHeight(node->right);
        if (leftHeight == -1 || rightHeight == -1 || abs(leftHeight - rightHeight) > 1) 
        {
            return -1;
        }
        else 
        {
            return max(leftHeight, rightHeight) + 1;
        }
    }
    
    bool isBalanced(TreeNode* root) 
    {
        return getHeight(root) >= 0;
    }
};