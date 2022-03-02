'''
0051 N-Queens
Must-have, so classic
# Const space? As n = 1, 2, ..., 9
# Just use it?
# Row is okay, we just loop through it
# Collections to record "placed" on column
# main diagonal: (row, col) row - col --> unique hash key
# alter diagonal: (row, col) row + col --> unique hash key
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def generateBoard():
            '''
            Out:
                board, a solution to the problem
            '''
            board = list()
            for i in range(n):
                # Here, row refers to each row of the board
                # queens is the column info
                rows[queens[i]] = 'Q'
                board.append("".join(rows))
                rows[queens[i]] = '.'
            return board
        
        def backtrack(row):
            if row == n:
                board = generateBoard()
                solutions.append(board)
            else:
                # Loop through possible column position
                # At current row
                for j in range(n):
                    # j -> columnSet
                    # row - j -> main diagonal
                    # row + j -> alt diagonal
                    if j in columnSet or row - j in diag1 or row + j in diag2:
                        continue
                    # Possible location
                    queens[row] = j
                    columnSet.add(j)
                    diag1.add(row - j)
                    diag2.add(row + j)
                    backtrack(row + 1)
                    # backtrack
                    diag1.remove(row - j)
                    diag2.remove(row + j)
                    columnSet.remove(j)
        solutions = list()
        columnSet = set()
        diag1 = set()
        diag2 = set()
        queens = [-1] * n
        rows = ['.'] * n
        backtrack(0)
        return solutions
