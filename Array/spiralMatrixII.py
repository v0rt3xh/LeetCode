'''
0059 Spiral Matrix II
'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        left, right, up, bottom = 0, n - 1, 0, n - 1
        start = 1
        while left < n and right > -1 and up < n and bottom > -1:
            for i in range(left, right + 1):
                res[up][i] = start
                start += 1
            up += 1
            if up > n - 1:
                break
            for k in range(up, bottom + 1):
                res[k][right] = start
                start += 1
            right -= 1
            if right < 0:
                break
            for l in range(right, left - 1, -1):
                res[bottom][l] = start
                start += 1
            bottom -= 1
            if bottom < 0:
                break
            for m in range(bottom, up - 1, -1):
                res[m][left] = start
                start += 1
            left += 1
        return res