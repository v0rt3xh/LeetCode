/**
0386 Lexicographical Numbers
Behind the scene is DFS
*/
class Solution 
{
public:
    vector<int> lexicalOrder(int n) 
    {
        //
        vector<int> result(n);
        int number = 1;
        for (int index = 0; index < n; index++) 
        {
            result[index] = number;
            // Try to add 0
            if (10 * number <= n) 
            {
                number *= 10;
            }
            else 
            {   
                // This loop means that
                // We have enumerate possible numbers @ the last digit's level
                // Need to go back
                // E.g, n = 120, we at 119, 1190 > 120, we are in the loop
                // 119 -> 11. Next number: start by 12. (Case 1)
                // E.g. n = 15, current number 15, cannot proceed to add 1
                // Go back a level.
                while (number % 10 == 9 || number + 1 > n) 
                {
                    number /= 10;
                }
                // Next number in lexicographical order
                number++;
            }
        }
        return result;
        
    }
};