/**
0405 Convert a Numebr to Hexadecimal
Digit manipulation
in binary representation: 32 digits
4 digits -> 8 groups 
Set each group to its hexadecimal form.
(nums >> (4 * i)) & 0xf
Leading zeros? Remember to check it. 
*/
class Solution 
{
public:
    string toHex(int num) 
    {
        if (num == 0) 
        {
            return "0";
        }
        string stringBuilder; 
        for (int i = 7; i > -1; i--) 
        {
            // Convert
            int val = (num >> (4 * i)) & 0xf;
            if (stringBuilder.length() > 0 || val > 0) 
            {
                char digit = val < 10 ? (char) ('0' + val) : (char) ('a' + val - 10);
                stringBuilder.push_back(digit);
            }
            
        }
        return stringBuilder;
    }
};