'''
0090 Subsets II
pruning at its finest
'''
# Official solution, easier to understand
# but, harder to derive the pruning condition
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def recur(prev, cur, index):
            # prev: boolean value suggesting if we have choose prev element
            if index == n:
                res.append(cur[:])
                return
            # Do not use current one
            recur(False, cur, index + 1)
            # did not use prev and same value as previous index
            # prune
            if not prev and index > 0 and nums[index] == nums[index - 1]:
                return
            cur.append(nums[index])
            recur(True, cur, index + 1)
            cur.pop()
        res = []
        nums.sort() # Avoid duplicates, we definitely need to sort.
        n = len(nums)
        recur(False, [], 0)
        return res

# more straight forward method:
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []  #存放符合条件结果的集合
        path = []  #用来存放符合条件结果
        def backtrack(nums,startIndex):
            res.append(path[:])
            for i in range(startIndex,len(nums)):
                if i > startIndex and nums[i] == nums[i - 1]:  #我们要对同一树层使用过的元素进行跳过
                    continue
                path.append(nums[i])
                backtrack(nums,i+1)  #递归
                path.pop()  #回溯
        nums = sorted(nums)  #去重需要排序
        backtrack(nums,0)
        return res

作者：carlsun-2
链接：https://leetcode-cn.com/problems/subsets-ii/solution/90-zi-ji-iiche-di-li-jie-zi-ji-wen-ti-ru-djmf/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。