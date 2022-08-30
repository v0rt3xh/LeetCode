/**
0623 Add One Row to Tree
BFS should be okay.
Well, we only need to reach depth - 1, then stop lol.
 */
class Solution 
{
public:
    TreeNode* addOneRow(TreeNode* root, int val, int depth) 
    {
        if (depth == 1) 
        {
            return new TreeNode(val, root, nullptr);
        }
        // Efficient Stack
        vector<TreeNode*> curLevel(1, root);
        for (int i = 1; i < depth - 1; i++) 
        {
            vector<TreeNode*> nextLevel; 
            for (auto &node: curLevel) 
            {
                if (node->left != nullptr) 
                {
                    nextLevel.emplace_back(node->left);
                }
                if (node->right != nullptr) 
                {
                    nextLevel.emplace_back(node->right);
                }
            }
            curLevel = move(nextLevel);
        }
        for (auto &node: curLevel) 
        {
            node->left = new TreeNode(val, node->left, nullptr);
            node->right = new TreeNode(val, nullptr, node->right);
        }
        return root;
    }
};