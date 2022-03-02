'''
0078 Subsets
Given an integer array nums of unique elements, 
return all possible subsets (the power set).

The solution set must not contain duplicate subsets. 
Return the solution in any order.

Good practice for doing dfs sort of stuffs.
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(cur, index):
            if index == n:
                res.append(cur[:])
                return
            cur.append(nums[index])
            dfs(cur, index + 1)
            cur.pop()
            dfs(cur, index + 1)
        
        dfs([], 0)
        return res
            
# Iterative approach or BFS

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        q=[[]]
        n=len(nums)
        for i in range(n):
            for j in range(len(q)):
                q.append(q[j]+[nums[i]])
        return q