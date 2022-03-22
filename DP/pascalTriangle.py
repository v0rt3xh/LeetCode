'''
0118 Pascal's Triangle
notice that
dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
'''
# Not elegant solution
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        res = [[1], [1, 1]]
        for i in range(3, numRows + 1):
            curlevel = [0] * i
            for j in range(i):
                value = 0
                if j - 1 >= 0:
                    value += res[i - 2][j - 1]
                if j <= i - 2:
                    value += res[i - 2][j]
                curlevel[j] = value
            res.append(curlevel)
        return res

'''
Better style
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = list()
        for i in range(numRows):
            # length i + 1
            level = list()
            for j in range(i + 1):
                if j == 0 or j == i:
                    level.append(1)
                else:
                    level.append(res[i - 1][j] + res[i - 1][j - 1])
            res.append(level)
        return res
