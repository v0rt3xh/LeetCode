/**
0543 Diameter of Binary Tree
A decent problem.
For each node, the path can be computed as:
It's left subtree's depth (L) + right (R) subtree's depth + 1
Maintain a variable for result,
we traverse through all the nodes. 
All 'node' act as root for once
*/
class Solution 
{
    int result; // number of nodes we can have in a path
public:
    int depth(TreeNode* node) 
    {
        if (node == nullptr) 
        {
            return 0; // Reach the end
        }
        int left_depth = depth(node->left); // recursive step.
        int right_depth = depth(node->right);
        result = max(result, left_depth + right_depth + 1); // Update node count
        return max(left_depth, right_depth) + 1; // Notice this,
        // We are returning depth!
    }
    int diameterOfBinaryTree(TreeNode* root) 
    {
        result = 1;
        depth(root);
        return result - 1; // We need to -1 to get length.
    }
};