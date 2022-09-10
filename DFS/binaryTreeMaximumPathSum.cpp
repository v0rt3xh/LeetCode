/**
 * 0124 Binary Tree Maximum Path Sum
 */
class Solution 
{
    int result = INT_MIN;
public:
    int maxGain(TreeNode* node) 
    {
        if (node == nullptr) 
        {
            return 0;
        }
        int leftGain = max(maxGain(node->left), 0);
        int rightGain = max(maxGain(node->right), 0);
        result = max(result, leftGain + rightGain + node->val);
        return max(leftGain, rightGain) + node->val;
    }
    
    int maxPathSum(TreeNode* root) 
    {
        maxGain(root);
        return result;
    }
};