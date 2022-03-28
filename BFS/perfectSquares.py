'''
0279 Perfect Squares
'''
import math
class Solution:
    def numSquares(self, n: int) -> int:
        '''
        Bellman Equation:
        dp[n] = dp[n - closest_PS] + 1? Not correct!
        Might Exceed Time limit's solution:
        '''
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            j = 1
            minvalue = float('inf') 
            while j * j <= i:
                minvalue = min(dp[i - j * j], minvalue)
                j += 1
            dp[i] = minvalue + 1
        return dp[n]
'''
Any place for improvement?
A BFS approach
Credit: 努力德国找实习, 自来火 @ leetcode-CN
'''
class Solution:
    def numSquares(self, n: int) -> int:
        from collections import deque
        deq = deque()
        visited = set()
        
        deq.append((n, 0))
        # element1: Current number, element2: Steps to reach
        while deq:
            number,step = deq.popleft()
            # possible targets / i, such that i * i < number
            targets = [number - i * i for i in range(1, int(number ** 0.5)+1)]
            for target in targets:
                # Only 0 included
                # return current step + 1
                if target == 0:return step + 1
                # for those not visited states, append more unit
                if target not in visited:
                    deq.append((target,step + 1))
                    visited.add(target)
        return 0
'''
Behind the scene
Credit: 子潇有话要说 @ leetcode-CN
       7              targets = [7 - 1, 7 - 2 * 2]
       / \ 
      6   3           targets_6 = [6 - 1, 6 - 2 * 2], targets_3 = [1]
    / \    \
   5   2    2         ...
  / \   \    \
1    4   1    1       for 1, targets = [0], just return
The depth of the tree, is what we need!
'''