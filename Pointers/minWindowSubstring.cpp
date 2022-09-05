/**
0076 Minimum Window Substring
Cpp version. 
Sliding Window.
*/

class Solution 
{
public:
    unordered_map<char, int> curFreq, givenFreq;
    bool checkCondition() 
    {
        // Check if current window substring includes given string.
        for (const auto& pairs: givenFreq) 
        {
            if (curFreq[pairs.first] < pairs.second) 
            {
                return false;
            }
        }
        return true;
    }
    string minWindow(string s, string t) 
    {
        // Initialize given frequency table.
        for (const auto& c: t) 
        {
            givenFreq[c]++;
        }
        int left = 0, right = -1;
        int length = INT_MAX, result_left = -1;
        while (right < int(s.size())) 
        {
            if (givenFreq.find(s[++right]) != givenFreq.end()) 
            {
                ++curFreq[s[right]];
            }
            // Compress
            while (checkCondition() && left <= right) 
            {
                if (right - left + 1 < length) 
                {
                    length = right - left + 1;
                    result_left = left;
                }
                if (givenFreq.find(s[left]) != givenFreq.end()) 
                {
                    --curFreq[s[left]];
                }
                left++;
            }
        }
        
        return result_left == -1 ? string() : s.substr(result_left, length);
    }
};