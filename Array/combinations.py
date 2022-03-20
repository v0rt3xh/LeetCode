'''
0077 Combinations
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, path):
            '''
            Some operations are redundant, 
            Not an optimized version.
            '''
            '''
            A basic pruning method:
            Cannot get k elements! 
            if len(path) + n - start < k:
                return
            '''
            if start >= n:
                '''
                Check if path length == k
                '''
                if len(path) == k:
                    # Append if conditino satisfied
                    res.append(path[:])
                return
            path.append(start + 1)
            backtrack(start + 1, path)
            path.pop()
            backtrack(start + 1, path)
        res = []
        backtrack(0, [])
        return res