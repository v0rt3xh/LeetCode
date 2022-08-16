/**
0778 Swim in Rising Water
Solve with Union Find,
Check if is possible to connect (0,0) and (n-1,n-1)
within the given threshold.
Therefore, we can iterate through threshold
Connect nodes if possible:
    First preprocess: put all the elevation into a vector
    Store the position of that elevation,
    e.g. elevation[4] = (1, 0) means in position (1, 0),
         The elevation is 4. 
    Then, iterate through threshold, connect those positions:
        threshold = 0:
        Check nearby position of x0, y0, if elevation <= threshold,
        connect.
*/

class Solution 
{
public:
    int find(vector<int>& parent, int node) 
    {
        if (parent[node] == node) 
        {
            return node;
        }
        int parent_node = find(parent, parent[node]);
        parent[node] = parent_node;
        return parent_node;
    }
    
    void merge(vector<int>& parent, int node1, int node2) 
    {
        int parent1 = find(parent, node1), parent2 = find(parent, node2);
        parent[parent1] = parent2;
    }
    
    int swimInWater(vector<vector<int>>& grid) 
    {
        int length = grid.size();
        // init union find's parent
        // Notice that we are considering position!
        vector<int> parent(length * length);
        for (int i = 0; i < length * length; i++) 
        {
            parent[i] = i;
        }
        
        // Preprocess, store height. 
        vector<pair<int, int>> elevations(length * length);
        for (int i = 0; i < length; i++) 
        {
            for (int j = 0; j < length; j++) 
            {
                elevations[grid[i][j]] = make_pair(i, j);
            }
        }
        
        // Iterate through threshold
        // Define directions:
        vector<pair<int,int>> directions{{0, -1}, {0, 1}, {1, 0}, {-1, 0}};
        for (int i = 0; i < length * length; i++) 
        {
            auto [x, y] = elevations[i];
            for (const auto [dx, dy]: directions) 
            {
                int newx = x + dx, newy = y + dy;
                if (newx < length && newx > -1 && newy < length && newy > -1 && grid[newx][newy] <= i) 
                {
                    merge(parent, x * length + y, newx * length + newy);
                }
            }
            if (find(parent, 0) == find(parent, length * length - 1)) 
            {
                return i;
            }
        }
        return -1;
        
        
    }
};