/**
0438 Find All Anagrams in a String
Sliding Window, WOW
*/

class Solution 
{
public:
    vector<int> findAnagrams(string s, string p) 
    {
        int m = s.size(), n = p.size();
        if (m < n) // Special Case
        {
            return {};
        }
        vector<int> pTable(26);
        for (auto c : p) 
        {
            pTable[c - 'a']++;
        }
        vector<int> result;
        for (int left = 0, right = 0; right < m; right++) 
        {
            --pTable[s[right] - 'a'];
            while (pTable[s[right] - 'a'] < 0) // Need to shrink
            {
                ++pTable[s[left] - 'a'];
                left++;
            }
            if (right - left + 1 == n) // Window size matches p's size 
            {
                // Append the result.
                result.push_back(left);
            }
        }
        return result;
    }
};