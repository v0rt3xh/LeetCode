'''
0032 Longest Valid Parentheses
DP Approach 
    dp[i]: the length of valid parentheses ending with str[i]
    init: all zeros, only str[i] == ')' dp[i] > 0 possible
    Bellman equation:
    1.  str[i] == ')' and str[i - 1] == '(',
        dp[i] = dp[i - 2] + 2
    2.  str[i] == ')' and str[i - 1] == ')':
        use dp[i - 1] to find the previous '('
        if str[i - dp[i - 1] - 1] == '(' // Matchable
            dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2:
            return 0
        n = len(s)
        # init
        dp = [0 for _ in range(n)]
        for i in range(1, n):
            # The corner case (when i == 1)
            # can be handled with ease! at the start dp[-1] = 0
            if s[i] == ')' and s[i - 1] == '(':
                dp[i] = dp[i - 2] + 2
            # A critical step -> do not let i - dp[i - 1] - 1 becomes negative.
            if s[i] == ')' and s[i - 1] == ')' and i - dp[i - 1] - 1 >= 0:
                if s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
        return max(dp)

'''
Stack approach
A more traditional approach
    Maintain a stack, in which the bottom element is index of the last unmatched ')'
    Other elements: the indices of '(' 
    Every time we meet a '(', push its index to the stack
    Every time we meet a ')', pop the element from the stack:
        if empty stack -> fail to match, update bottom element
        else right index - left index + 1 -> the length of str ending with current ')'
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2:
            return 0
        n = len(s)
        # pre_place -1, help us solve the corner case
        # i.e, at first meet ( & )
        # 1 - (-1) = 2
        # or meet ), directly change to the closest unmatched )
        stack = [-1]
        length = 0
        for i in range(n):
            # if left (, push to the stack
            if s[i] == '(':
                stack.append(i)
            else:
                # meet a ), pop off corresponding '('
                stack.pop()
                if not stack: # unmatched )
                    stack.append(i)
                else:
                    left = stack[-1] # ( or ) before ()
                    # i - left (the matched '(' ) + 1
                    # i.e. i - (left - 1), the top element in the stack.
                    length = max(length, i - left)
        return length