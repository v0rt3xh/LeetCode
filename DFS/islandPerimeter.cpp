/**
0463 Island Perimeter
Every contiguous island cell will -2 perimeter
1. Iterate through the grid, 
meet an island, island_count += 1
meet a contiguous island, contiguous_count += 1
return 4 * island - 2 * contiguous_count
*/
class Solution 
{
public:
    int islandPerimeter(vector<vector<int>>& grid) 
    {
        int island_count = 0, contiguous_count = 0;
        for (int i = 0; i < grid.size(); i++) 
        {
            for (int j = 0; j < grid[0].size(); j++) 
            {
                if (grid[i][j] == 1) 
                {
                    island_count += 1;
                    if ((i + 1) < grid.size()) 
                    {
                        if (grid[i + 1][j] == 1) 
                        {
                            contiguous_count += 1;
                        }
                    }
                    if ((j + 1) < grid[0].size()) 
                    {
                        if (grid[i][j + 1] == 1) 
                        {
                            contiguous_count += 1;
                        }                        
                    }
                }
            }
        }
        return 4 * island_count - 2 * contiguous_count;
    }
};

/**
0463 Island Perimeter
2. DFS,
Start from an island:
meet next island: perimeter gain + 2
meet ocean / out of index: perimeter gain + 1
meet previous: gain + 0
Credit:
作者：LeetCode-Solution
链接：https://leetcode.cn/problems/island-perimeter/solution/dao-yu-de-zhou-chang-by-leetcode-solution/
来源：力扣（LeetCode）
*/
class Solution2 {
    constexpr static int dx[4] = {0, 1, 0, -1};
    constexpr static int dy[4] = {1, 0, -1, 0};
public:
    int dfs(int x, int y, vector<vector<int>> &grid, int n, int m) {
        if (x < 0 || x >= n || y < 0 || y >= m || grid[x][y] == 0) {
            return 1;
        }
        if (grid[x][y] == 2) {
            return 0;
        }
        grid[x][y] = 2;
        int res = 0;
        for (int i = 0; i < 4; ++i) {
            int tx = x + dx[i];
            int ty = y + dy[i];
            res += dfs(tx, ty, grid, n, m);
        }
        return res;
    }
    int islandPerimeter(vector<vector<int>> &grid) {
        int n = grid.size(), m = grid[0].size();
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (grid[i][j] == 1) {
                    ans += dfs(i, j, grid, n, m);
                }
            }
        }
        return ans;
    }
};
