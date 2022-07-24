/**
0515 Find Largest Value in Each Tree Row
DFS / BFS both okay,
DFS will need height information.
 */
class Solution 
{
public:
    void dfs(TreeNode *node, vector<int> &result, int curHeight) 
    {
        if (curHeight == result.size()) 
        {
            // Reach a new height, directly push to the result array
            result.push_back(node->val);
        }
        else 
        {
            result[curHeight] = max(result[curHeight], node->val);
        }
        // Start recursive steps
        if (node->left) 
        {
            dfs(node->left, result, curHeight + 1);
        }
        if (node->right) 
        {
            dfs(node->right, result, curHeight + 1);
        }
    }
    vector<int> largestValues(TreeNode* root) 
    {
        if (!root) 
        {
            return {};
        }
        vector<int> result;
        dfs(root, result, 0);
        return result;
    }
};