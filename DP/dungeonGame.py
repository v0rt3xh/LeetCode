'''
0174 Dungeon Game
Python Version
'''
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row, col = len(dungeon), len(dungeon[0])
        DP = [[5001] * (col + 1) for _ in range(row + 1)]
        DP[row][col - 1] = DP[row - 1][col] = 1
        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                nextStep = min(DP[i + 1][j], DP[i][j + 1])
                DP[i][j] = max(nextStep - dungeon[i][j], 1)
        return DP[0][0]