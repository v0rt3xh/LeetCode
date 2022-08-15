/**
0461 Hamming Distance
1. Built-in algorithm

*/

class Solution 
{
public:
    int hammingDistance(int x, int y) 
    {
        return __builtin_popcount(x ^ y); 
    }   
};

/**
0461 Hamming Distance
2. Brian Kernighan algorithm
*/

class Solution 
{
public:
    int hammingDistance(int x, int y) 
    {
        int result = 0, tmp = x ^ y;
        while (tmp) 
        {
            tmp = tmp & (tmp - 1);
            result += 1;
        }
        return result;
    }   
};

