'''
0036 Valid Sudoku
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row hash
        # Col hash
        # Maze hash
        hashSet = dict()
        for i in range(9):
            hashSet[i] = []
        for i in range(10, 19):
            hashSet[i] = []
        for i in range(3):
            for j in range(3):
                hashSet[(i, j)] = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] not in hashSet[i]:
                        hashSet[i].append(board[i][j])
                    else:
                        return False
                    if board[i][j] not in hashSet[j + 10]:
                        hashSet[j + 10].append(board[i][j])
                    else:
                        return False
                    if board[i][j] not in hashSet[(i//3, j//3)]:
                        hashSet[(i//3, j//3)].append(board[i][j])
                    else:
                        return False
        return True