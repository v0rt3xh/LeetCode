'''
0091 Decode Ways
I mean, can we simplify those if/else?.
Sure you can.
'''
# My dumb version
class Solution:
    def numDecodings(self, s: str) -> int:
        # Have I seen you before??
        # Deal with leading zero first ...
        n = len(s)
        if s[0] == '0':
            return 0
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            prev = int(s[i - 1 : i + 1])
            if s[i] == '0':
                if prev == 0 or prev > 26:
                    return 0
                else:
                    # did not use sentinel, so...
                    if i - 2 >= 0:
                        dp[i - 1] = dp[i - 2]
                        dp[i] = dp[i - 1]
                    else:
                        dp[i] = dp[i - 1] = 1
            else:
                if s[i - 1] == '0' or prev > 26:
                    dp[i] = dp[i - 1]
                else:
                    if i - 2 >= 0:
                        dp[i] = dp[i - 2] + dp[i - 1]
                    else:
                        dp[i] = dp[i - 1] + 1
        return dp[-1]

# smart as F version:
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # one serve as a sentinel in some sense
        f = [1] + [0] * n
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                # notice that i - 1 in fact is s[i], as we used
                # sentinel. Thus, at least can plus previous ways.
                f[i] += f[i - 1]
            if i > 1 and s[i - 2] != '0' and int(s[i-2:i]) <= 26:
                # s[i - 1] is not 0, then, we can add 
                # the corresponding dp value of s[i - 2]
                # add more stuff
                f[i] += f[i - 2]
        # damn that was smart
        return f[n]
'''
CREDIT: 
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/decode-ways/solution/jie-ma-fang-fa-by-leetcode-solution-p8np/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''