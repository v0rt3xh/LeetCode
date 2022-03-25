'''
0119 Pascal's Triangle II
'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        queue = [] # Store previous row
        for i in range(rowIndex + 1):
            level = [] # current level
            for j in range(i + 1):
                if j > 0 and j < i:
                    level.append(queue[j] + queue[j - 1])
                else:
                    level.append(1)
            queue = level
        return queue

'''
O(rowIndex) Extra space?
'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        r = [1] # base
        # [i][j] = [i - 1][j - 1] + [i - 1][j]
        # Thus, compute from the right end!
        for i in range(rowIndex):
            r.append(0) # expand current list
            j = i + 1 # start from the right
            # modify from the last element!
            while j > 0:
                r[j] = r[j] + r[j - 1]
                j -= 1
        return r
'''
Credit: KyrieX @ Leetcode-CN
'''