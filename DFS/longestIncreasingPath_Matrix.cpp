/**
 * 0329 Longest Increasing Path in a Matrix
 * DFS + Memo! Important to know
 * Credit: Leetcode.cn - solution
 */
class Solution {
public:
    // Useful variables
    static constexpr int dirs[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    int rows, columns; 
    
    int longestIncreasingPath(vector<vector<int>>& matrix) 
    {
        rows = matrix.size();
        columns = matrix[0].size();
        // Create a memo
        auto memo = vector<vector<int>> (rows, vector<int>(columns));
        int result = 0;
        // Compute result through iterating different starting point
        for (int i = 0; i < rows; i++) 
        {
            for (int j = 0; j < columns; j++) 
            {
                result = max(result, dfs(matrix, i, j, memo));
            }
        }
        return result;
    }
    
    int dfs(vector<vector<int>> &matrix, int row, int column, vector< vector<int> > &memo) 
    {
        if (memo[row][column] != 0) 
        {
            // If we have previous result, just return
            return memo[row][column];
        }
        // Otherwise add value and init.
        ++memo[row][column];
        for (int i = 0; i < 4; i++) 
        {
            int newRow = row + dirs[i][0], newColumn = column + dirs[i][1];
            if (newRow > -1 && newRow < rows && newColumn > -1 && newColumn < columns && matrix[newRow][newColumn] > matrix[row][column]) 
            {
                // Find the right direction and update.
                memo[row][column] = max(memo[row][column], dfs(matrix, newRow, newColumn, memo) + 1);
            }
        }
        return memo[row][column];
    }
};
