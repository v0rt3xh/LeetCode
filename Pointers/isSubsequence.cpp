/**
0392 Is Subsequence
We maintain two pointers. 
Different starting points? 
No need to consider it, if subsequence is valid,
we will get the answer by traversing from the first junction.
*/
class Solution 
{
public:
    bool isSubsequence(string s, string t) 
    {
        if (s.size() > t.size()) 
        {
            return false;
        }
        int cursor_s = 0, cursor_t = 0;
        while (cursor_t < t.size()) 
        {
            if (s[cursor_s] == t[cursor_t]) 
            {
                cursor_s++;
            }
            cursor_t++;
            if (cursor_s == s.size()) 
            {
                return true;
            }
        }
        return s.size() + t.size() == 0 ? true : false;
        
    }
};

// Dp approach for the follow-up
/**
 * dp[i][j], starting from the i-th position, 
 * the next position where j-th character appears 
 * dp[i][j] = i. if t[i] is the j-th character
 * Otherwise dp[i][j] = dp[i + 1][j]
 * init, suppose size of t: m
 * dp[m][~] = m;
 * Credit: Leetcode CN
 */
/**
作者：LeetCode-Solution
链接：https://leetcode.cn/problems/is-subsequence/solution/pan-duan-zi-xu-lie-by-leetcode-solution/
来源：力扣（LeetCode）*/
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int n = s.size(), m = t.size();

        vector<vector<int> > f(m + 1, vector<int>(26, 0));
        for (int i = 0; i < 26; i++) {
            f[m][i] = m;
        }

        for (int i = m - 1; i >= 0; i--) {
            // Preprocess t
            for (int j = 0; j < 26; j++) {
                if (t[i] == j + 'a')
                    f[i][j] = i;
                else
                    f[i][j] = f[i + 1][j];
            }
        }
        int add = 0; // current starting point in s 
        for (int i = 0; i < n; i++) {
            if (f[add][s[i] - 'a'] == m) { // Would not appear, just false
                return false;
            }
            add = f[add][s[i] - 'a'] + 1; // Jump to the next starting point
        }
        return true;
    }
};

