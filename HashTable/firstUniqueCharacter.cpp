/**
0387 First Unique Character in a String
HashMap
traverse two times.
*/
class Solution 
{
public:
    int firstUniqChar(string s) 
    {
        vector<int> hashMap(26, 0);
        for (auto c: s) 
        {
            hashMap[c - 'a']++;
        }
        for (int i = 0; i < s.length(); i++)  
        {
            if (hashMap[s[i] - 'a'] == 1) 
            {
                return i;
            }
        }
        return -1;
    }
};