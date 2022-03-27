'''
0212 Combination Sum III
'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(path, start, target):
            # Stopping conditions
            curLen = len(path)
            if start > 9 or curLen >= k or target <= 0:
                if target == 0 and curLen == k:
                    res.append(path[:])
                return
            # Operations
            path.append(start)
            backtrack(path, start + 1, target - start)
            path.pop()
            backtrack(path, start + 1, target)
        backtrack([], 1, n)
        return res
