/**
0423 Reconstruct Original Digits from English
Feels like solving equations.
0 2 4 6 8: z, w, u, x g
1: Count['O'] - Count[0] - Count[4] - Count[2]
9: Count['i'] - Count[5] - Count[6] - Count[8]
3: Count['h'] - Count[8]
5: Count['f'] - Count[4]
7: Count['s'] - Count[6]
*/
class Solution {
public:
    string originalDigits(string s) 
    {
        unordered_map<char, int> counter;
        for (char c : s) 
        {
            counter[c]++;
        }
        vector<int> frequency(10);
        frequency[0] = counter['z'];
        frequency[2] = counter['w'];
        frequency[4] = counter['u'];
        frequency[6] = counter['x'];
        frequency[8] = counter['g'];
        
        frequency[3] = counter['h'] - frequency[8];
        frequency[5] = counter['f'] - frequency[4];
        frequency[7] = counter['s'] - frequency[6];
        
        frequency[1] = counter['o'] - frequency[0] - frequency[2] - frequency[4];  
        frequency[9] = counter['i'] - frequency[5] - frequency[6] - frequency[8];
        string result;
        for (int i = 0; i < 10; i++) 
        {
            for (int j = 0; j < frequency[i]; j++) 
            {
                result += char(i + '0');
            }
        }
        return result;
    }
};