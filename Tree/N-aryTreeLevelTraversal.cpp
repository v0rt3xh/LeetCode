/**
0429 N-ary Tree Level Order Traversal
BFS
*/

class Solution 
{
public:
    vector<vector<int>> levelOrder(Node* root) 
    {
        if (!root) 
        {
            return {};
        }
        queue<Node*> working_queue;
        working_queue.push(root);
        vector<vector<int>> res;
        while (!working_queue.empty()) 
        {
            vector<int> level_result;
            int level_size = working_queue.size();
            for (int i = 0; i < level_size; i++) 
            {
                Node* node = working_queue.front();
                working_queue.pop();
                level_result.push_back(node->val);
                for (Node *child : node->children) 
                {
                    working_queue.push(child);
                }
            }
            // Efficient Transfer
            res.push_back(move(level_result));
        }
        return res;
    }
};