/**
0473 Matchsticks to Square
Backtrack
- First compute the total length of the matchsticks.
- If total_length % 4 != 0, just false
- Then, maintain an edges array of length 4.
- edge_length = total_length / 4
- sort the matchsticks array for a faster process.
- for each stick in the matchstick array,
- add it to one of the edge in edges array.
*/

class Solution 
{
public:
    bool dfs(int index, vector<int> &matchsticks, vector<int> &edges, int length) 
    {
        if (index == matchsticks.size()) 
        {
            return true;
        }
        // Add to the edge array, try if the stick can fit in
        for (int i = 0; i < edges.size(); i++) 
        {
            edges[i] += matchsticks[index];
            if (edges[i] <= length && dfs(index + 1, matchsticks, edges, length)) 
            {
                return true;
            }
            // Remember to remove the edge and proceed to the other edges.
            edges[i] -= matchsticks[index];
        }
        return false;
    }
    
    bool makesquare(vector<int>& matchsticks) 
    {
        int totalLength = accumulate(matchsticks.begin(), matchsticks.end(), 0);
        if (totalLength % 4 != 0) 
        {
            return false;
        }
        sort(matchsticks.begin(), matchsticks.end(), greater<int>());
        vector<int> edges(4);
        return dfs(0, matchsticks, edges, totalLength / 4);
    }
    
};