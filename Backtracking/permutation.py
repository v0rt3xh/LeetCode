'''
0046 Permutation

'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(numList, curList):
            if len(numList) < 1:
                res.append(curList[:])
                return
            n = len(numList)
            for i in range(n):
                curList.append(numList[i])
                backtrack(numList[:i] + numList[(i + 1):], curList)
                curList.pop()
        if len(nums) == 1:
            return [nums]

        backtrack(nums, [])
        return res

# Smarter
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0):
            # 所有数都填完了
            if first == n:  
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        res = []
        backtrack()
        return res