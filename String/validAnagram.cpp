/**
 * 0242 Valid Anagram 
 * alphabet frequency array
 * iterate through s and t.
 * the final array should have all elements 0 if true.
 */

class Solution {
public:
    bool isAnagram(string s, string t) 
    {
        vector<int> alphabet(26);
        int n = s.length(), m = t.length();
        if (n != m) 
        {
            return false;
        }
        for (int i = 0; i < n; i++) 
        {
            int index = s[i] - 'a';
            alphabet[index] += 1; 
        }
        for (int j = 0; j < m; j++)
        {
            int index = t[j] - 'a';
            alphabet[index] -= 1;
        }
        for (int i = 0; i < 26; i++) 
        {
            if (alphabet[i] != 0) 
            {
                return false;
            }
        }
        return true;
    }
};