'''
0304 Range Sum Query 2D - Immutable
'''

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])
        self.prefixSum = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                self.prefixSum[i][j] += matrix[i][j]
                if i - 1 > -1:
                    self.prefixSum[i][j] += self.prefixSum[i - 1][j]
                if j - 1 > -1:
                    self.prefixSum[i][j] += self.prefixSum[i][j -1]
                if i - 1 > -1 and j - 1 > -1:
                    self.prefixSum[i][j] -= self.prefixSum[i - 1][j - 1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.prefixSum[row2][col2]
        if col1 - 1 > -1:
            result -= self.prefixSum[row2][col1 - 1]
        if row1 - 1 > -1:
            result -= self.prefixSum[row1 - 1][col2]
        if row1 - 1 > -1 and col1 - 1 > -1:
            result += self.prefixSum[row1 - 1][col1 - 1]
        return result
        