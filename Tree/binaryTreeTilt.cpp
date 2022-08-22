/**
 * 0563 Binary Tree Tilt
 DFS Approach
 Recursive step compute sum of left subtree and right subtree,
 Current sum as the return value,
 Update total tilt along the way.
 */
class Solution {
public:
    int result = 0;
    int findTilt(TreeNode* root) 
    {
        getTilt(root);
        return result;
    }
    int getTilt(TreeNode* root) 
    {
        if(root == nullptr) 
        {
            return 0;
        }
        int left = getTilt(root->left);
        int right = getTilt(root->right);
        result += abs(left - right);
        return root->val + left + right;        
    }
};