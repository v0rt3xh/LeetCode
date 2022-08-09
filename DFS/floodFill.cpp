/**
0733 Flood Fill
DFS
*/
class Solution 
{
public:
    const int delta_row[4] = {1, 0, 0, -1};
    const int delta_col[4] = {0, 1, -1, 0};
    int chosen_color; 
    void dfs(vector<vector<int>>& image, int row, int col, int color) 
    {
        if (image[row][col] == color) 
        {
            return;
        }
        if (image[row][col] == chosen_color) 
        {
            image[row][col] = color;
            for (int i = 0; i < 4; i++) 
            {
                int new_row = row + delta_row[i], new_col = col + delta_col[i];
                if (new_row < image.size() && new_row > -1 && new_col < image[0].size() && new_col > -1) 
                {
                    dfs(image, new_row, new_col, color);
                }
            }
        }
    }
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) 
    {
        chosen_color = image[sr][sc];
        dfs(image, sr, sc, color);
        return image;
    }
};


/**
 * Official solution, faster.
 */

class Solution2 {
public:
    const int dx[4] = {1, 0, 0, -1};
    const int dy[4] = {0, 1, -1, 0};
    void dfs(vector<vector<int>>& image, int x, int y, int color, int newColor) {
        if (image[x][y] == color) {
            image[x][y] = newColor;
            for (int i = 0; i < 4; i++) {
                int mx = x + dx[i], my = y + dy[i];
                if (mx >= 0 && mx < image.size() && my >= 0 && my < image[0].size()) {
                    dfs(image, mx, my, color, newColor);
                }
            }
        }
    }

    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        int currColor = image[sr][sc];
        if (currColor != newColor) {
            dfs(image, sr, sc, currColor, newColor);
        }
        return image;
    }
};

/**
Reference：LeetCode-Solution
Link：https://leetcode.cn/problems/flood-fill/solution/tu-xiang-xuan-ran-by-leetcode-solution/
*/