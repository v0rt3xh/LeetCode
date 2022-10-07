'''
01444 Number of Ways of Cutting a Pizza
Tiktok OA Last Question
DP + Prefix Sum
Use LRU Cache to save some time.
'''

class Solution:
    def ways(self, pizza: List[str], K: int) -> int:
        # m, n, mod: row, col, the number to mod.
        m, n, MOD = len(pizza), len(pizza[0]), 10 ** 9 + 7
        # Prefix Sum, Prefix[i][j]: Number of Apples in the Array[i:][j:]
        preSum = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                preSum[r][c] = preSum[r][c + 1] + preSum[r + 1][c] - preSum[r + 1][c + 1] + (pizza[r][c] == 'A')

        @lru_cache(None)
        def dp(k, r, c):
            # This function stands for: Number of ways of cutting
            # on subArray[r:][c:], using k cuts
            if preSum[r][c] == 0: return 0 # No Apple, invalid
            if k == 0: return 1 # No cuts, enough, return 1
            ans = 0
            # cut horizontally
            for nr in range(r + 1, m):
                # When there is at least one apple in upper region, cut
                if preSum[r][c] - preSum[nr][c] > 0:
                    ans = (ans + dp(k - 1, nr, c)) % MOD
            # cut vertically                    
            for nc in range(c + 1, n):
                # When there is at least one apple in the left region
                if preSum[r][c] - preSum[r][nc] > 0:
                    ans = (ans + dp(k - 1, r, nc)) % MOD
            return ans

        return dp(K - 1, 0, 0)