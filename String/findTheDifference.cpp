/**
0389 Find the difference
Count / Sum / XOR operation
*/
class Solution 
{
public:
    char findTheDifference(string s, string t) 
    {
        int result = 0;
        for (char c: s) 
        {
            result ^= c;
        }
        for (char c: t) 
        {
            result ^= c;
        }
        return result;
    }
};
