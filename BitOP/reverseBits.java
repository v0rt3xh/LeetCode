/* 
0190 Reverse Bits
*/

// Bit manipulations 

public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int rev = 0; // result
        for (int i = 0; i < 32 && n != 0; ++i) {
            // Add the result to rev
            rev |= (n & 1) << (31 - i);
            // Move to the right 
            n >>>= 1;
        }
        return rev;
    }
}