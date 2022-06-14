/**
0404 Sum of Left Leaves
DFS & BFS Approaches
 */
class SolutionDFS 
{
public:
    bool isLeafNode(TreeNode* node) 
    {
        return !node->left && !node->right;
    }
    
    int dfs(TreeNode* node) 
    {
        int ans = 0;
        if (node->left) 
        {
            ans += isLeafNode(node->left) ? node->left->val : dfs(node->left);
        }
        if (node->right && !isLeafNode(node->right)) 
        {
            ans += dfs(node->right);
        }
        return ans;
    }
    
    int sumOfLeftLeaves(TreeNode* root) 
    {
        return root ? dfs(root) : 0;
    }
};

class SolutionBFS 
{
public:
    int sumOfLeftLeaves(TreeNode* root) 
    {
        queue<TreeNode*> workQueue; 
        workQueue.push(root);
        int result = 0;
        while (!workQueue.empty()) 
        {
            TreeNode* node = workQueue.front();
            workQueue.pop();
            if (node->left) 
            {
                workQueue.push(node->left);
                if (!node->left->left && !node->left->right) 
                {
                    result += node->left->val;
                }
            }
            if (node->right) 
            {
                workQueue.push(node->right);
            }
        }
        return result;
    }
};