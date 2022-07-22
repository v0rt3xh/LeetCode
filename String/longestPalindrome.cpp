/**
0409 Longest Palindrome
Count even frequency characters
+1 if we can 
*/
class Solution 
{
public:
    int longestPalindrome(string s) 
    {
        unordered_map<char, int> frequency;
        int result = 0;
        for (char c : s) 
        {
            frequency[c]++;
        }
        for (auto element: frequency) 
        {
            int value = element.second;
            result += value / 2 * 2;
        }
        if (result < s.length()) 
        {
            result += 1;
        }
        return result;
    }
};