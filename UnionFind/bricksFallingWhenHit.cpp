/**
0803 Bricks Falling When Hit
Union Find
Approach this problem in a reverse direction.
*/

class UnionFind 
{
private:
    vector<int> f, sz; // f: parent node.
                       // sz[i]: number of nodes that have i as the parent.
public:
    UnionFind(int n): f(n), sz(n) 
    {
        for (int i = 0; i < n; i++) 
        {
            f[i] = i;
            sz[i] = 1; // init all sizes are one.
        }
    }

    int find(int x) 
    {
        if (f[x] == x) 
        {
            return x;
        }
        int newf = find(f[x]);
        f[x] = newf;
        return f[x];
    }

    void merge(int x, int y) 
    {
        int fx = find(x), fy = find(y);
        if (fx == fy) 
        {
            return;
        }
        f[fx] = fy;
        // Now we need to add up the sizes.
        sz[fy] += sz[fx];
    }

    int size(int x) 
    {
        // Only parent node's size is meaningful.
        return sz[find(x)];
    }
};

class Solution 
{
public:
    vector<int> hitBricks(vector<vector<int>>& grid, vector<vector<int>>& hits) 
    {
        int h = grid.size(), w = grid[0].size();
        
        UnionFind uf(h * w + 1); // Mapping from 2D to 1D.
        vector<vector<int>> status = grid;
        for (int i = 0; i < hits.size(); i++) {
            status[hits[i][0]][hits[i][1]] = 0; // We approach this problem in a reverse fashion.
        }
        for (int i = 0; i < h; i++) 
        {
            for (int j = 0; j < w; j++) 
            {
                if (status[i][j] == 1) 
                {
                    if (i == 0) 
                    {
                        // Connect to a super node (Top grid)
                        uf.merge(h * w, i * w + j);
                    }
                    if (i > 0 && status[i - 1][j] == 1) 
                    {
                        uf.merge(i * w + j, (i - 1) * w + j);
                    }
                    if (j > 0 && status[i][j - 1] == 1) 
                    {
                        uf.merge(i * w + j, i * w + j - 1);
                    }
                }
            }
        }
        const vector<pair<int, int>> directions{{0, 1},{1, 0},{0, -1},{-1, 0}};
        vector<int> ret(hits.size(), 0);
        for (int i = hits.size() - 1; i >= 0; i--) 
        {   // Reverse thinking
            int r = hits[i][0], c = hits[i][1];
            if (grid[r][c] == 0) 
            {
                // hit nothing, cannot introduce new bricks
                continue;
            }
            // Record previous size
            int prev = uf.size(h * w);

            if (r == 0) 
            {   // connect to super node
                uf.merge(c, h * w);
            }
            for (const auto [dr, dc]: directions) 
            {
                int nr = r + dr, nc = c + dc;
                
                if (nr >= 0 && nr < h && nc >= 0 && nc < w) 
                {
                    if (status[nr][nc] == 1) 
                    {   // Merge adjacent nodes. 
                        uf.merge(r * w + c, nr * w + nc);
                    }
                }
            }
            // Get current size
            int size = uf.size(h * w);
            ret[i] = max(0, size - prev - 1);
            // Add the node to current status.
            status[r][c] = 1;
        }
        return ret;
    }
};
/**
Credit：LeetCode-Solution
Link：https://leetcode.cn/problems/bricks-falling-when-hit/solution/da-zhuan-kuai-by-leetcode-solution-szrq/
*/