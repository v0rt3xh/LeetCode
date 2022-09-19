/**
 * 0236 Lowest Common Ancestor of a Binary Tree
 Stop blowing my mind.
 */
class Solution 
{
public:
    TreeNode* LCA;
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) 
    {
        dfs(root, p, q);
        return LCA;
    }
    bool dfs(TreeNode* node, TreeNode* p, TreeNode* q) 
    {
        if (node == nullptr) 
        {
            return false;
        }
        // Start recursive step;
        bool leftSon = dfs(node->left, p, q);
        bool rightSon = dfs(node->right, p, q);
        if ((leftSon && rightSon) || ((node->val == p->val || node->val == q->val) && (leftSon || rightSon))) 
        {
            LCA = node;
        }
        return leftSon || rightSon || node->val == p->val || node->val == q->val;
    }
};