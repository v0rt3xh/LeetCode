/**
0513 Find Bottom Left Tree Value
DFS, get the node with the largest height (or depth)
First one it's definitely the leftmost one
 */
class Solution {
public:
    // Good usage of '&'
    void dfs(TreeNode *node, int height, int &curValue, int &curHeight) 
    {
        if (node == nullptr) 
        {
            return;
        }
        height++;
        dfs(node->left, height, curValue, curHeight);
        dfs(node->right, height, curValue, curHeight);
        if (height > curHeight) 
        {
            // Achieve the current highest height
            // Update & set value
            curHeight = height;
            curValue = node->val;
        }
    }
    
    
    int findBottomLeftValue(TreeNode* root) 
    {
        int curHeight = 0, curValue = 0;
        dfs(root, 0, curValue, curHeight); 
        return curValue;
    }
};