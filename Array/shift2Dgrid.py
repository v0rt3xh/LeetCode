''''
1260 Shift 2D Grid
'''
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        # Special case
        if k == 0 or k % (m * n) == 0:
            return grid
        tool = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # next column is easy to retrieve
                nextCol = (j + k) % n
                # but, what about row?
                # first compute how many rows we need to move
                # take the modulo w.r.t row number
                moveRow = (j + k) // n
                nextRow = (i + moveRow) % m
                tool[nextRow][nextCol] = grid[i][j]
        return tool