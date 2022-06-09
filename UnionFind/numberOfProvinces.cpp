/**
0547 Number of Provinces
1.DFS / 2. Union Find
*/

class Solution1
{
public:
    int findCircleNum(vector<vector<int>>& isConnected) 
    {
        // Number of cities
        int cities = isConnected.size();
        // Visited array
        vector<int> visited(cities);
        // init value: 0
        int province = 0;
        for (int i = 0; i < cities; i++) 
        {
            if (!visited[i]) // Meet city in new province, explore and add up
            {
                dfs(isConnected, visited, cities, i);
                province++;
            }
            
        }
        return province;
    }

    // dfs
    void dfs(vector<vector<int>>& isConnected, vector<int>& visited, int cities, int i) 
    {
        for (int j = 0; j < cities; j++) 
        {   // Mark only when not visited and has connection
            if (!visited[j] && isConnected[i][j] == 1) 
            {
                visited[j] = 1;
                dfs(isConnected, visited, cities, j);
            }
        }
    }
};

class Solution2 
{
public:
    int Find(vector<int>& parent, int index) 
    {
        // When parent is not itself, 
        // recursively search upper / parents
        if (parent[index] != index) 
        {
            parent[index] = Find(parent, parent[index]);    
        }
        return parent[index];
    }
    
    void Union(vector<int>& parent, int node1, int node2) 
    {   // Union two nodes
        parent[Find(parent, node1)] = Find(parent, node2);
    }
    
    int findCircleNum(vector<vector<int>>& isConnected) 
    {
        int cities = isConnected.size();
        vector<int> parent(cities);
        int province = 0;
        // init parent array. parent == node itself
        for (int i = 0; i < cities; i++) 
        {
            parent[i] = i;
        }
        for (int i = 0; i < cities; i++) 
        {
            for (int j = i + 1; j < cities; j++) 
            {
                // If connect, union.
                if (isConnected[i][j] == 1) 
                {
                    Union(parent, i, j);
                }
            }
        }
        // Get the number of provinces by checking union set parents
        for (int i = 0; i < cities; i++) 
        {
            if (parent[i] == i) 
            {
                province++;
            } 
        }
        return province;
    }
    
};
