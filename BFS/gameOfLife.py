'''
0289 Game of Life
'''
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''
        0 - 0: Previously dead, still dead
        1 - 1: Previously alive, still alive
        0 - *: Previously dead, turn to live
        1 - #: previously alive, turn to dead
        '''
        def bfs(x, y):
            count = 0
            '''
            Not really a BFS, just eight neighbors :)
            '''
            eight = [(x - 1,y - 1), (x - 1,y), (x - 1,y + 1),
                    (x, y - 1),(x, y + 1),
                    (x + 1,y - 1), (x + 1,y), (x + 1,y + 1)]
            for row, col in eight:
                if row > -1 and col > -1 and row < m and col < n:
                    # Notice that # is a previous 1.
                    if board[row][col] == 1 or board[row][col] == '#':
                        count += 1
            return count
        
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                # Update current state
                # following the rules
                numLive = bfs(i, j)
                # 1 -> 0: '#'
                if numLive < 2 and board[i][j] == 1:
                    board[i][j] = '#'
                elif numLive > 3 and board[i][j] == 1:
                    board[i][j] = '#'
                # 0 -> 1: '*
                elif numLive == 3 and board[i][j] == 0:
                    board[i][j] = '*'
        # Update to the next state
        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 0
                elif board[i][j] == '*':
                    board[i][j] = 1
