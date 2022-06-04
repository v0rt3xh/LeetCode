'''
Worth Reviewing
0329 Longest Increasing Path in a Matrix
'''
class Solution:

    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Constrain on the moving directions
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # dfs with memoization
        @lru_cache(None)
        def dfs(row, col):
            best = 1
            for delta_r, delta_c in DIRECTIONS:
                next_r, next_c = row + delta_r, col + delta_c
                if -1 < next_r < m and -1 < next_c < n and matrix[next_r][next_c] > matrix[row][col]:
                    best = max(best, dfs(next_r, next_c) + 1)
            return best
        
        result = 0
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))
        return result
        
        
        
                
        