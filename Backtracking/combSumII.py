'''
0040 Combination Sum II
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def recur(index, margin, curList):
            # margin is 0, just append the result
            if margin == 0:
                res.append(curList[:])
                return
            # Check current possible branches
            for i in range(index, n):
                # if larger element, just stop
                if candidates[index] > margin:
                    break
                # repeated recursive step, remove it!
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                # backtrack step
                curList.append(candidates[i])
                # i + 1: next starting point
                recur(i + 1, margin - candidates[i], curList)
                curList.pop()
        res = []
        n = len(candidates)
        # sorting helps us!
        candidates.sort()
        recur(0, target, [])
        return res
                