/**
 * 0530 Minimum Absolute Difference in BST
 DFS, keep track of previous node's value
 And the result
 use reference &
 */
class Solution {
public:
    int getMinimumDifference(TreeNode* root) 
    {
        int pre = -1, result = INT_MAX;
        dfs(pre, root, result);
        return result;
    }
    
    void dfs(int& pre, TreeNode *node, int &result) 
    {
        if (node == nullptr) 
        {
            return;
        }
        dfs(pre, node->left, result);
        if (pre == -1) 
        {   // init
            pre = node->val;
        }
        else 
        {   // update result if we can
            result = min(result, node->val - pre);
            // move 'pre'
            pre = node->val;
        }
        dfs(pre, node->right, result);
    }
};