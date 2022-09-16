/**
0200 Number of Islands
Last time, we use BFS,
this time, try DFS.
We do not introduce a visited array,
Modify in-place, could be a problem. 
*/

class Solution 
{
public:
    void dfs(vector<vector<char>>& grid, int row, int col) 
    {
        // All we have to do, it's set zero and examine the neighbors!
        int rowLength = grid.size();
        int colLength = grid[0].size();
        
        grid[row][col] = '0';
        if (row - 1 > -1 && grid[row - 1][col] == '1') dfs(grid, row - 1, col);
        if (row + 1 < rowLength && grid[row + 1][col] == '1') dfs(grid, row + 1, col);
        if (col - 1 > -1 && grid[row][col - 1] == '1') dfs(grid, row, col - 1);
        if (col + 1 < colLength && grid[row][col + 1] == '1') dfs(grid, row, col + 1);
    }
    int numIslands(vector<vector<char>>& grid) 
    {
        // Then, just traverse through the grid, problem solved. Nice
        int rowLength = grid.size();
        int colLength = grid[0].size();
        int numOfIslands = 0;
        for (int i = 0; i < rowLength; i++) 
        {
            for (int j = 0; j < colLength; j++) 
            {
                if (grid[i][j] == '1') 
                {
                    numOfIslands += 1;
                    dfs(grid, i, j);
                }
            }
        }
        return numOfIslands;
    }
};