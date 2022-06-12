/**
0306 Additive Number
Credit: @LeetCode-Solution
The first number, second number, and length determine the sequence.
Input sequence with length n, 
first: the first number; 
    - Starting at: firstStart = 0,
    - End at: firstEnd
second: the second number;
    - Starting at: secondStart = firstEnd + 1
    - End at secondEnd.
We need to iterate w.r.t 
    - All the possible second Start and second End
Sanity check:
    - compute the sum of first and second (third) using string addition.
    - compare third with the remaining digits
    - Too long / not match: bye bye
    - Exact: True
    - Some digit in num get leftbehind, update firstEnd/Start, secondEnd/Start,
    - continue the process.
*/
class Solution {
public:
    bool isAdditiveNumber(string num) {
        int n = num.size();
        // Range of second start [1, n - 2]
        for (int secondStart = 1; secondStart < n - 1; ++secondStart) {
            // No leading zero possible
            if (num[0] == '0' && secondStart != 1) {
                break;
            }
            for (int secondEnd = secondStart; secondEnd < n - 1; ++secondEnd) {
                // Exclude leading zero
                if (num[secondStart] == '0' && secondStart != secondEnd) {
                    break;
                }
                if (valid(secondStart, secondEnd, num)) {
                    return true;
                }
            }
        }
        return false;
    }

    bool valid(int secondStart, int secondEnd, string num) {
        // Sanity check
        int n = num.size();
        int firstStart = 0, firstEnd = secondStart - 1;
        while (secondEnd <= n - 1) {
            string third = stringAdd(num, firstStart, firstEnd, secondStart, secondEnd);
            int thirdStart = secondEnd + 1;
            int thirdEnd = secondEnd + third.size();
            if (thirdEnd >= n || !(num.substr(thirdStart, thirdEnd - thirdStart + 1) == third)) {
                // Terminate condition
                break;
            }
            if (thirdEnd == n - 1) {
                // exact match
                return true;
            }
            // There are remaining digits in num, continute examining.
            firstStart = secondStart;
            firstEnd = secondEnd;
            secondStart = thirdStart;
            secondEnd = thirdEnd;
        }
        return false;
    }

    string stringAdd(string s, int firstStart, int firstEnd, int secondStart, int secondEnd) {
        // Helper method for computing the sum of digits. 
        string third;
        int carry = 0, cur = 0;
        while (firstEnd >= firstStart || secondEnd >= secondStart || carry != 0) {
            cur = carry;
            if (firstEnd >= firstStart) {
                cur += s[firstEnd] - '0';
                --firstEnd;
            }
            if (secondEnd >= secondStart) {
                cur += s[secondEnd] - '0';
                --secondEnd;
            }
            carry = cur / 10;
            cur %= 10;
            third.push_back(cur + '0');
        }
        reverse(third.begin(), third.end());
        return third;
    }
};
/**
Link：https://leetcode.cn/problems/additive-number/solution/lei-jia-shu-by-leetcode-solution-cadc/
