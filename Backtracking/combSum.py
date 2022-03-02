'''
0039 Combination sum
----
    Use current candidates or do not use current candidates
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def recur(current, index):
            # index out of bound of larger sum -> comes to an end
            if index >= len(candidates) or sum(current) >= target:
                if sum(current) == target:
                    # append the result
                    res.append(current[:])
                return
            # split 1: use current index
            current.append(candidates[index])
            recur(current, index)
            current.pop()
            # split 2: do not use current index!
            recur(current, index + 1)
        recur([], 0)
        return res