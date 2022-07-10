/**
0695 Max Area of Island
BFS 
*/

class Solution 
{
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) 
    {
        int m = grid.size(), n = grid[0].size();
        int result = 0;
        for (int i = 0; i < m; i++) 
        {
            for (int j = 0; j < n; j++) 
            {
                if (grid[i][j] == 1) 
                {
                    int cur_area = 0;
                    queue<int> queue_x;
                    queue<int> queue_y;
                    grid[i][j] = 0;
                    queue_x.push(i);
                    queue_y.push(j);
                    while (!queue_x.empty()) 
                    {
                        int island_x = queue_x.front(), island_y = queue_y.front();
                        queue_x.pop();
                        queue_y.pop();
                        cur_area += 1;
                        int delta_x[4] = {0, 0, 1, -1};
                        int delta_y[4] = {1, -1, 0, 0};
                        for (int index = 0; index < 4; index++) 
                        {
                            int next_x = island_x + delta_x[index], next_y = island_y + delta_y[index];
                            if (next_x < m && next_x > -1 && next_y < n && next_y > -1 && grid[next_x][next_y] == 1)
                            {
                                grid[next_x][next_y] = -1;
                                queue_x.push(next_x);
                                queue_y.push(next_y);
                            }
                        }
                    }
                                result = max(result, cur_area);
                }

                
            }
        }
                                return result;
        
    }

};