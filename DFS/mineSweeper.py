'''
0529 Minesweeper
DFS
'''

# Directions
SURROUNDINGS = [(0, 1), (0, -1), (1, 0), (-1, 0),
                (-1, -1), (-1, 1), (1, 1), (1, -1)]

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def dfs(row, col):
            # If meet an underlying mine, just end
            if board[row][col] == 'M':
                return
            # Only explore when empty
            if board[row][col] == 'E':
                value = 0 # Surrounding mine's number
                nextOnes = [] # Record what coordinates are feasible for next steps.
                for delta_row, delta_col in SURROUNDINGS:
                    new_row, new_col = delta_row + row, delta_col + col
                    if -1 < new_row < m and -1 < new_col <n:
                        nextOnes.append((new_row, new_col)) # feasible next steps
                        if board[new_row][new_col] == 'M':
                            value += 1
                if value: # Adjacent mines
                    board[row][col] = str(value)
                else:
                    # Blank
                    board[row][col] = 'B'
                    for new_row, new_col in nextOnes:
                            dfs(new_row, new_col)
            return
        # Special case, pretty rare? 1st step on mine
        start_row, start_col = click
        if board[start_row][start_col] == 'M':
            board[start_row][start_col] = 'X'
            return board
        m, n = len(board), len(board[0])
        dfs(start_row, start_col)
        return board