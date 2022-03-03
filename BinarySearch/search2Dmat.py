'''
0074 Search a 2D matrix
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        An observation: the top right corner
        "left": small, "right": large
        '''
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j > -1:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                return True
        return False