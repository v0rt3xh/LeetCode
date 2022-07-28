/**
0542 01 Matrix
Sometimes, you need to pay attention to the description
Nearest Distance -> Oh wow BFS
Focus on 0 -> retrieve the value for 1's!
DP optimization possible
*/

class Solution1
{
private:
    // Moving directions
    static constexpr int delta[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) 
    {
        int m = mat.size(), n = mat[0].size();
        // Distance result
        vector<vector<int>> distance(m, vector<int>(n));
        // Visited set
        vector<vector<int>> visited(m, vector<int>(n));
        // Working queue
        queue<pair<int, int>> working_queue;
        // At first, we put all the zeros into the queue
        for (int i = 0; i < m; i++) 
        {
            for (int j = 0; j < n; j++) 
            {
                if(mat[i][j] == 0) 
                {
                    working_queue.emplace(i, j);
                    visited[i][j] = 1;
                }
            }
        }
        // Then find the smallest distance for each 1
        while (!working_queue.empty()) 
        {
            auto [i, j] = working_queue.front();
            working_queue.pop();
            for (int index = 0; index < 4; index++) 
            {
                int next_row = i + delta[index][0], next_col = j + delta[index][1];
                if (next_row < m && next_row > -1 && next_col < n && next_col > -1 && !visited[next_row][next_col]) 
                {
                    // Notice we have visited 0's before, so they will be ignored
                    distance[next_row][next_col] = distance[i][j] + 1;
                    working_queue.emplace(next_row, next_col);
                    visited[next_row][next_col] = 1;
                }
            }
        }
        return distance;
    }
};

class Solution2 
/**
DP solution, for a 1 to reach closest 0:
    either ONLY move left move up 
    either ONLY move left move down
    either ONLY move right move up
    either ONLY move right move down
    WOW!
*/
{
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) 
    {
        int m = matrix.size(), n = matrix[0].size();
        // INIT DP ARRAY WITH INT_MAX / 2
        vector<vector<int>> dist(m, vector<int>(n, INT_MAX / 2));
        // element is 0, then 0
        for (int i = 0; i < m; ++i) 
        {
            for (int j = 0; j < n; ++j) 
            {
                if (matrix[i][j] == 0) 
                {
                    dist[i][j] = 0;
                }
            }
        }
        // left and up
        // Control dp's direction!
        for (int i = 0; i < m; ++i) 
        {
            for (int j = 0; j < n; ++j) 
            {
                if (i - 1 >= 0) 
                {  // moved from previous left
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1);
                }
                if (j - 1 >= 0) 
                {  // moved from previous up
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1);
                }
            }
        }
        // left and down
        for (int i = m - 1; i >= 0; --i) // reverse i's direction
        {
            for (int j = 0; j < n; ++j) 
            {
                if (i + 1 < m) 
                {
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1);
                }
                if (j - 1 >= 0) 
                {
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1);
                }
            }
        }
        // Only right and up
        for (int i = 0; i < m; ++i) 
        {
            for (int j = n - 1; j >= 0; --j) 
            {
                if (i - 1 >= 0) 
                {
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1);
                }
                if (j + 1 < n) 
                {
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1);
                }
            }
        }
        // only right and down
        for (int i = m - 1; i >= 0; --i) 
        {
            for (int j = n - 1; j >= 0; --j) 
            {
                if (i + 1 < m) 
                {
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1);
                }
                if (j + 1 < n) 
                {
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1);
                }
            }
        }
        return dist;
    }
};
/**
Credit：zerotrac2 @ LeetCode-Solution 
Link：https://leetcode.cn/problems/01-matrix/solution/01ju-zhen-by-leetcode-solution/
*/