'''
0048 Rotate Image
Tricky boi!
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 1:
            return
        # Rotation one, horizontal flip
        mid = n // 2
        for i in range(mid):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i -1][j], matrix[i][j]
        # Main diagnoal filp
        for i in range(n - 1):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                