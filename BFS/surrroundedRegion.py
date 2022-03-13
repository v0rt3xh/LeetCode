'''
0130 Surrounded Region
At first, I did not use the property of those zeros on the boundaries
:(
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Surrounded regions should not be on the border, 
        which means that any 'O' on the border of the board are not flipped to 'X'
        1. For every boundary O's, we mark its adjacent O's by a symbol 'H'
        'H' stands for non-surrounded region, need to restore
        2. Then, we need to flip the leftover O's to X's
        """
        def recur(i, j):
            if i < 0 or i > m - 1 or j < 0 or j > n - 1 or board[i][j] != 'O':
                return
            board[i][j] = 'H'
            recur(i - 1, j)
            recur(i + 1, j)
            recur(i, j - 1)
            recur(i, j + 1)
        # start the recursive procedure on boundaries
        m, n = len(board), len(board[0])
        for i in range(m):
            recur(i, 0)
            recur(i, n - 1)
        for i in range(n):
            recur(0, i)
            recur(m - 1, i)
        # last step, restore or flip it
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'H':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
'''
Credit:
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/surrounded-regions/solution/bei-wei-rao-de-qu-yu-by-leetcode-solution/
来源：力扣（LeetCode）
'''