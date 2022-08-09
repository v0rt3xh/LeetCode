/**
0526 Beautiful Arrangement
Backtrack. 
Adding to index. 
In python, I pass in a list as a syntax, backtrack(index, helper_list)
that's slow.
We can preprocess and use a set to help us
*/

class Solution 
{
public:
    vector<vector<int>> match; // Store the matching element for each index
    vector<int> visited; // store the elements we have seen
    int num; // result
    void backtrack(int index, int n) 
    {
        if (index == n + 1) 
        {
            num += 1;
            return;
        }
        for (auto &x: match[index]) 
        {
            if (!visited[x]) 
            {   
                visited[x] = 1;
                backtrack(index + 1, n);
                visited[x] = 0; // restore
            }
            
        }
    }
    
    int countArrangement(int n) 
    {
        visited.resize(n + 1);
        match.resize(n + 1);
        for (int i = 1; i < n + 1; i++) 
        {
            for (int j = 1; j < n + 1; j++) 
            {
                if (i % j == 0 || j % i == 0) 
                {
                    match[i].push_back(j);
                }
            }
        }
        backtrack(1, n);
        return num;
        
    }
};