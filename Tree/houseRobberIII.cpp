/**
0337 House Robber III
DP in a tree structure.
For a node: either selected / not selected: f / g
- When selected:
    f(node) = g(node.left) + g(node.right)
- When not selected:
    f(node) = max(g(node.left), f(node.left)) + max(g(node.right), f(node.right))
 */
class Solution 
{
public:
    unordered_map<TreeNode*, int> f, g;
    void dfs(TreeNode* node) 
    {
        if (!node) 
        {
            return;
        }
        dfs(node->left);
        dfs(node->right);
        // Select!
        f[node] = node->val + g[node->left] + g[node->right];
        g[node] = max(g[node->left], f[node->left]) + max(g[node->right], f[node->right]);
    }
    
    int rob(TreeNode* root) 
    {
        dfs(root);
        return max(f[root], g[root]);
    }
};