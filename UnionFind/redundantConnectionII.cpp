/**
0685 Redundant Connection II
Credit: LeetcodeCN-Solution 
In this graph, every node has a parent node
except the root. After adding a redundant connection, 
we can observe that 
1. root could have a parent node. Cycle must be somewhere.
2. there is a node other than root, that has two parents. Could have cycle or do not have. 
We need to find the edge that leads to two parent or cycle.
*/
struct UnionFind
{
    vector<int> ancestors;
    
    UnionFind(int n) 
    {
        ancestors.resize(n);
        for (int i = 0; i < n; i++) 
        {
            ancestors[i] = i;
        }
    }
    
    int Find(int index) 
    {
        return index == ancestors[index] ? index : ancestors[index]=Find(ancestors[index]);
    }
    
    void Union(int index1, int index2) 
    {
        ancestors[Find(index1)] = Find(index2);
    }

};

class Solution 
{
public:
    vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) 
    {
        int num_edges = edges.size();
        UnionFind union_find = UnionFind(num_edges + 1);
        auto parent = vector<int>(num_edges + 1);
        for (int i = 1; i <= num_edges; i++) 
        {
            parent[i] = i;
        }
        int conflict = -1;
        int cycle = -1;
        for (int i = 0; i < num_edges; i++) 
        {
            auto edge = edges[i];
            int node1 = edge[0], node2 = edge[1];
            // node2's parent is not it self, conflict
            if (parent[node2] != node2) 
            {
                conflict = i;
            }
            else 
            {
                parent[node2] = node1;
                if (union_find.Find(node1) == union_find.Find(node2)) 
                {
                    // Find a cycle
                    cycle = i;
                }
                else 
                {
                    union_find.Union(node1, node2);
                }
            }
            
        }
        if (conflict < 0) 
        {
            // No conflict, return the cycle-causing edge
            auto redundant = vector<int>{edges[cycle][0], edges[cycle][1]};
            return redundant;
        }
        else 
        {
            auto conflictEdge = edges[conflict];
            if (cycle >= 0) 
            {
                // A cycle also exists
                auto redundant = vector<int>{parent[conflictEdge[1]], conflictEdge[1]};
                return redundant;
            }
            else 
            {
                auto redundant = vector<int>{conflictEdge[0], conflictEdge[1]};
                return redundant;
            }
        }
    }
};