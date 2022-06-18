/**
0684 Redundant Connection
Union Find.
If common parent occurs, just return that edge
*/

class Solution 
{
public:
    int Find (vector<int>& parent, int index) 
    {
        if (parent[index] != index)
        {
            parent[index] = Find(parent, parent[index]);
        }
        return parent[index];
    }
    
    void Union(vector<int>& parent, int index1, int index2) 
    {
        parent[Find(parent, index1)] = Find(parent, index2);
    }    
    
    vector<int> findRedundantConnection(vector<vector<int>>& edges) 
    {
        int num_edge = edges.size();
        vector<int> parent(num_edge + 1);
        // init parent
        for (int num = 1; num <= num_edge; num++) 
        {
            parent[num] = num;
        }
        for (auto& edge: edges) 
        {
            int node1 = edge[0], node2 = edge[1];
            if (Find(parent, node1) != Find(parent, node2)) 
            {
                Union(parent, node1, node2);
            }
            else 
            {
                return edge;
            }
        }
        return vector<int>{};
    }
};