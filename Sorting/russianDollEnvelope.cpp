/**
0354 Russian Doll Envelopes
Sorting & DP
Longest increasing subsequence. 
First sort by width (ascending)
Then sort by height (descending)
At last get the longest increasing subsequence on height's dimension.
O(N^2) if plain DP, optimized by binary search O(NlogN).
*/
class Solution 
{
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) 
    {
        // Prepocess
        int num_envelope = envelopes.size();
        sort(envelopes.begin(), envelopes.end(), [](const auto& e1, const auto& e2) 
             {
                return e1[0] < e2 [0] || (e1[0] == e2[0] && e1[1] > e2[1]);                        });
        // DP step
        // Suppose f[j]: the smallest last element of subsequence with length j
        // Formed by the first i element.
        // For current element height_i, 
        // height_i > element in f: append it.
        // Otherwise, find the largest element that is smaller than height_i
        // Append to corresponding location
        // init h0
        vector<int> f{envelopes[0][1]};
        for (int i = 1; i < num_envelope; i++) 
        {
            if (int num = envelopes[i][1]; num > f.back()) 
            {
                f.push_back(num);
            }
            else 
            {
                auto location = lower_bound(f.begin(), f.end(), num);
                *location = num;
            }
        }
        return f.size();
        
    }
};