/**
0371 Sum of Two Integers
Bit operation
*/
class Solution 
{
public:
    int getSum(int a, int b) 
    {
        while (b != 0) 
        {
            unsigned int carry = (unsigned int)(a & b) << 1;
            a = a ^ b;
            b = carry;
        }
        return a;
    }
};
/**
Credit: Leetcode Solution @ CN
Link: https://leetcode.cn/problems/sum-of-two-integers/solution/liang-zheng-shu-zhi-he-by-leetcode-solut-c1s3/
*/

class Solution2
{
public:
    int getSum(int a, int b) 
    {
        return b ? getSum(a ^ b, uint(a & b) << 1) : a;
    }
};

/**
Credit: Muriyatensei @ Leetcode CN
*/