/**
0400 Nth Digit
First, we locate our scope to 'k' digit number,
Then, we compute the digit with in that scope. 
*/
class Solution 
{
public:
    int findNthDigit(int n) 
    {
        int num_digit = 1, count = 9;
        while (n > (long) num_digit * count) 
        {
            n -= num_digit * count;
            num_digit++;
            count *= 10;
        }
        int index = n - 1;
        int starting_num = (int) pow(10, num_digit - 1);
        int num = starting_num + index / num_digit;
        int digitIndex = index % num_digit;
        int digit = (num / (int) (pow(10, num_digit - digitIndex - 1))) % 10;
        return digit;
        
    }
};