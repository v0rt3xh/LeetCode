/**
0424 Longest Repeating Character Replacement
Sliding window
*/
class Solution 
{
public:
    int characterReplacement(string s, int k) 
    {
        vector<int> frequency(26); // Store current frequencies
        int length = s.length();
        int most_freq = 0; // Current max
        int left = 0, right = 0;
        while (right < length) // move right cursor
        {
            frequency[s[right] - 'A']++;
            // get current most frequent value
            most_freq = max(most_freq, frequency[s[right] - 'A']);
            if (right - left + 1 - most_freq > k) 
            {
                // If not satisfy condition, compress left end by 1.
                // Key we want to keep current max interval shape.
                frequency[s[left] - 'A']--;
                left++;
            }
            right++;
        }
        return right - left; // no need + 1, cuz right = length
    }
};