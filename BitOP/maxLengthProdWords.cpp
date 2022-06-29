/**
0318 Maximum Product of Word Lengths
Cannot avoid O(n^2), 
Can we make checking words' common letters faster?
Bitmask
The lowest 26 digits as the signal of character appearance in a word.
*/

class Solution 
{
public:
    int maxProduct(vector<string>& words) 
    {
        // Build the bitmask
        int array_length = words.size();
        vector<int> masks(array_length);
        for (int i = 0; i < array_length; i++) 
        {
            string word = words[i];
            int word_length = word.size();
            for (int k = 0; k < word_length; k++) 
            {
                masks[i] |= 1 << (word[k] - 'a');
            }
        }
        int max_product = 0;
        for (int i = 0; i < array_length - 1; i++) 
        {
            for (int j = i; j < array_length; j++) 
            {
                // No common characters, then compare
                if ((masks[i] & masks[j]) == 0) 
                {
                    max_product = max(max_product, int(words[i].size() * words[j].size()));
                }
            }
        }
        return max_product;
        
    }
};