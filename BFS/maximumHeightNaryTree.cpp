/*
0559 Maximum Depth of N-ary Tree
BFS
*/

class Solution 
{
public:
    int maxDepth(Node* root) 
    {
        if (root == nullptr) 
        {
            return 0;
        }
        queue<Node*> workQueue;
        workQueue.push(root);
        int height = 0;
        while(!workQueue.empty()) 
        {
            int length = workQueue.size();
            height += 1;
            for (int i = 0; i < length; i++) 
            {
                Node* current_node = workQueue.front();
                workQueue.pop();
                for (auto child : current_node->children) 
                {
                    workQueue.push(child);
                }
            }
        }
        return height;
    }
};