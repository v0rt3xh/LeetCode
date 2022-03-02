'''
0042 Trapping Rain Water
Idea:
Find each position i,
compute its rainwater
leftmost max lm[i]
rightmost max rm[i]

min(lm[i], rm[i]) - height[i]

the naive way exceed time limit

any smarter idea??
'''
# Workable solution but time exceed lmao
# will optimize base on this!

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 2:
            return 0
        height.append(-1)
        height.insert(0, -1)
        res = 0
        for i in range(1, n + 1):
            # Find the leftMost_max and rightMost_max for each element.
            leftStack = None
            j = i - 1
            while j > -1:
                if not leftStack:
                    if height[j] >= height[i]:
                        leftStack = j
                else:
                    if height[j] >= height[leftStack]:
                        leftStack = j
                j -= 1
            k = i + 1
            rightStack = None
            while k < n + 2:
                if not rightStack:
                    if height[k] >= height[i]:
                        rightStack = k
                else:
                    if height[k] >= height[rightStack]:
                        rightStack = k
                k += 1
            if rightStack and leftStack:
                res += min(height[rightStack], height[leftStack]) - height[i]
        return res
                
# 1 DP improvement
'''
DP approach to get the leftmax and rightmax
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 2:
            return 0
        leftMax = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        rightMax = [0] * (n - 1) + [height[n - 1]]
        for j in range(n - 2, -1, -1):
            rightMax[j] = max(rightMax[j + 1], height[i])
        res = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        return res
                        
'''
ultimate god
double pointer & double variable

leftPtr, rightPtr
when meet stop
leftMax, rightMax
if height[left] < height[right]:
    leftMax < rightMax
    add leftMax - height[left] to the result
    left += 1
(else) if height[right] <= height[left]
    rightMax <= leftMax
    add rightMax - height[right] to the result
    right -= 1
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        left = 0
        right = n - 1
        res = 0
        leftMax = 0
        rightMax = 0
        while left < right:
            leftMax = max(height[left], leftMax)
            rightMax = max(height[right], rightMax)
            if height[left] < height[right]:
                res += leftMax - height[left]
                left += 1
            else:
                res += rightMax - height[right]
                right -= 1
        return res