'''
0037 sudoku solver
When using backtracking
dfs()
At each step, what are we doing?
In this case, 
at each position (possible fill-in stage):
    enumerate through nine possible numbers
    only when 'condition' satisfied, start the following operations (recur)
    => natural questions
        1. store the three different requirements
        2. initial positions
        3. recur / backtrack operations
'''

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # pos: x-th blank to fill-in
        def dfs(pos: int):
            nonlocal valid
            # When it comes to the end (no more spaces to fill up)
            if pos == len(spaces):
                valid = True
                return
            
            i, j = spaces[pos]
            for digit in range(9):
                if line[i][digit] == column[j][digit] == block[i // 3][j // 3][digit] == False:
                    # recur step pre
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True
                    # added element, not need restore, we can replace it
                    board[i][j] = str(digit + 1)
                    # recur step
                    dfs(pos + 1)
                    # restore setting
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = False
                if valid:
                    return

        # each line's number usage    
        line = [[False] * 9 for _ in range(9)]
        # each column's number usage
        column = [[False] * 9 for _ in range(9)]
        # block's number usage
        block = [[[False] * 9 for _a in range(3)] for _b in range(3)]
        valid = False
        # A list for us to store the positions
        spaces = list()

        # iterative step
        # get the positions
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    spaces.append((i, j))
                else:
                    # current number - 1 to help store!
                    digit = int(board[i][j]) - 1
                    # update the usage 
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True

        dfs(0)
