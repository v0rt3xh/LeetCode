/**
0412 Fizz Buzz
*/

class Solution {
public:
    vector<string> fizzBuzz(int n) 
    {
        vector<string> result;
        for (int i = 1; i < n + 1; i++) 
        {
            string current_result;
            if (i % 3 == 0) 
            {
                current_result += "Fizz";
            }
            if (i % 5 == 0) 
            {
                current_result += "Buzz";
            }
            if (current_result.size() == 0) 
            {
                current_result += to_string(i);
            }
            result.emplace_back(current_result);
        }
        return result;
    }
};