/**
0299 Bulls and Cows
0 - 9, 10 numbers, array serves as a natural hash table.
first iteration: 
find the number of bulls and 
add frequency of each number.
second iteration,
find the numbers that are either bull or cow
-   if hashTable[number] > 0,
    reduce hashTable[number] by 1.
    bulls_and_cows +1
At last bulls_and_cows - bulls = cows
*/
class Solution 
{
public:
    string getHint(string secret, string guess) 
    {
        int game_size = secret.length();
        vector<int> digit_collections(10, 0);
        int bulls = 0, bulls_cows = 0;
        for (int i = 0; i < game_size; i++) 
        {
            // Count frequency
            digit_collections[secret[i] - '0'] += 1;
            // Record Bulls
            if (secret[i] == guess[i]) 
            {
                bulls += 1;
            }
        }
        for (int i = 0; i < game_size; i++) 
        {
            // Reduce frequency
            // Add bulls and cows
            if (digit_collections[guess[i] - '0'] > 0) 
            {
                digit_collections[guess[i] - '0'] -= 1;
                bulls_cows += 1;
            }
        }
        return to_string(bulls) + "A" + to_string(bulls_cows - bulls) + "B";
    }
};