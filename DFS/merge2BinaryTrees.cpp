/**
 0617 Merge Two Binary Trees
 * My dfs version did not use new, 
 * So looks kinda weird.
 */
class Solution 
{
public:
    TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) 
    {
        if (root1 == nullptr && root2 == nullptr) 
        {
            // both nullptr case
            return nullptr;
        }
        TreeNode* newNode;
        if (root1 == nullptr) 
        {
            // only root2 necessary
            newNode = root2;
        }
        else if (root2 == nullptr) 
        {
            // only root1 necessay
            newNode = root1;
        }
        else 
        {
            // both available
            newNode = root1;
            newNode->val += root2->val;
        }
        newNode->left = mergeTrees(root1 == nullptr ? nullptr : root1->left, root2 == nullptr ? nullptr : root2->left);
        newNode->right = mergeTrees(root1 == nullptr ? nullptr : root1->right, root2 == nullptr ? nullptr : root2->right);
        return newNode;
    }
};

// Alternative

class Solution2 
{
public:
    TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) 
    {
        if (root1 == nullptr) 
        {
            return root2;
        }
        if (root2 == nullptr) 
        {
            return root1;
        } 
        auto newNode = new TreeNode(root1->val + root2->val);
        newNode->left = mergeTrees(root1->left, root2->left);
        newNode->right = mergeTrees(root1->right, root2->right);
        return newNode;
    }
};