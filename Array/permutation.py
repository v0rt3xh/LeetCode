'''
0047 permutation II
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(numList, curList):
            '''
            numList serves as the candidate list
            curList is the path or result we will append
            '''
            # Different from combination / subsets
            # We only append when the candidate list is empty
            if len(numList) < 1:
                res.append(curList[:])
                return
            n = len(numList) # Current length
            # we start the permutation process
            for i in range(n):
                # Not the starting index & repeated elements -> skip to prune
                if i > 0 and numList[i - 1] == numList[i]:
                    continue
                # Add current element
                curList.append(numList[i])
                backtrack(numList[:i] + numList[(i + 1):], curList)
                # restore
                curList.pop()
        if len(nums) == 1:
            return [nums]
        nums.sort() # Sort to remove duplicates.
        backtrack(nums, [])
        return res       