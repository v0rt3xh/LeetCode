/*
0135 Candy
Two rules: For two adjacent children A B (A is on B's left)
Rule one: When rating_A > rating_B: candy_A > candy_B
Rule two: when rating_B > rating_A: candy_A < candy_B
The candy distribution among children satisfies given rule:
Equivalent to satisfying Rule one and Rule two.
To do this: two rounds of traverse.
First from left to right, then right to left
*/
class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        vector<int> left(n); // init an array with size n
        // Start from left to right:
        for (int i = 0; i < n; i++) {
            // Case 1: Need to satisfy the rule.
            if (i > 0 && ratings[i] > ratings[i - 1]) {
                left[i] = left[i - 1] + 1;
            }
            // Case 2: one is enough.
            else {
                left[i] = 1;
            }
        }
        // Result stores the number we return
        // Right is a variable storing the number of candies in right neighbors.
        int result = 0;
        int right = 0; 
        // Start the second traversal
        for (int i = n - 1; i > -1; i--) {
            if (i < n - 1 && ratings[i] > ratings[i + 1]) {
                right++;
            }
            else {
                right = 1;
            }
            result += max(left[i], right);
        }
        return result;
    }
};