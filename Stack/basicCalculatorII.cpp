/*
0227 Basic Calculator II
Integer in the expression: All non-negative integers.
Multiply and divide prior than add and minus.
Use a stack to store the intermediate results,
Use a char variable to record previous operators.
*/
class Solution {
public:
    int calculate(string s) {
        vector<int> stack;
        char prevOp = '+'; // Default sign should be 'add'.
        int num = 0;
        int n = s.length();
        for (int i = 0; i < n; i++) {
            if (isdigit(s[i])) {
                // Keep add up the number.
                num = num *10 + int(s[i] - '0');
            }
            if (!isdigit(s[i]) && s[i] != ' ' || i == n - 1) {
                // Encouter operators
                switch(prevOp) {
                    case '+': 
                        stack.push_back(num);
                        break;
                    case '-':
                        stack.push_back(-num);
                        break;
                    case '*':
                        // meet multiply, directly compute result
                        stack.back() *= num;
                        break;
                    default:
                        stack.back() /= num;  
                }
                // Need to change the operator and restore num
                prevOp = s[i];
                num = 0;
            }
        }
        return accumulate(stack.begin(), stack.end(), 0);
    }
};