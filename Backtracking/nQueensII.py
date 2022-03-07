'''
0052 N-Queens II
Like a review of N-Queens

'''
class Solution:
    def __init__(self):
        self.count = 0
    def totalNQueens(self, n: int) -> int:
        def backtrack(row):
            if row == n:
                self.count += 1
            else:
                for j in range(n):
                    if j in colSet or row - j in diag1 or row + j in diag2:
                        continue
                    colSet.add(j)
                    diag1.add(row - j)
                    diag2.add(row + j)
                    backtrack(row + 1)
                    colSet.remove(j)
                    diag1.remove(row - j)
                    diag2.remove(row + j)
        
        colSet = set()
        diag1 = set()
        diag2 = set()
        backtrack(0)
        return self.count