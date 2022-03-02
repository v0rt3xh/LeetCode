'''
005 Longest Palindromic Substring
'''

# Two dimensional DP I assume ... 
# Don't have to be the output directly
# Could be a helper measure,
# Here dp[i, j] IS Longest Palindromic Substring i, j 
# Then, what is the Bellman Equation?
# dp[i, i]: true
# one center as well as two centers
# if j - i < 2
# dp[i, j] = dp[i + 1, j - 1] && match
# dp[i, i + 1] = s[i] == s[i + 1]
# How to retrieve the max result string?
# take care of the length! start 

# Problem: how to iterate? how to store the maxLen etc.

class Solution():
    def longestPalindrome(self, s):
        n = len(s)
        if n < 2: # Special Case!
            return s
        # Record helper
        max_len = 1
        begin = 0
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n): # init
            dp[i][i] = True
        
        # 递推开始
        # 先枚举子串长度 IMPORTANT
        for L in range(2, n + 1):
            # Exceed running time on Leetcode USA :(
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break
                    
                if s[i] != s[j]:
                    dp[i][j] = False 
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                
                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]

'''
Another approach: save memory space -> 中心扩散法
Traverse through all the centers!
one - center 
two - center

class Solution():
    # Define a helper method that helps us
    # expand the center!
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s):
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]
        
'''
