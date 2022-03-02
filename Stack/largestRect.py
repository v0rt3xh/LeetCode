'''
0084 Largest Rectangle in Histogram
'''
# 1 Brutal-Force Method
# We expand each rectangle -> "Find the largest possible areas
# for all the rectangles." O(N^2)
# 2 Monotone Stack Method
# Get in the elements,
# Once we meet a element smaller than current stack top's element
# pop the element and compute the area
# Find the left 'smaller' component as well
# (rightIndex - leftIndex - 1) * poped element's height
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        # Append two sentinels, avoid corner cases.
        heights = [0] + heights + [0]
        stack = [0] # Our stack store the index! Init with sentinel
        size += 2
        res = 0
        # iterate throught the heights array
        for i in range(1, size):
            # If meet 'lower' height, pop!
            while heights[i] < heights[stack[-1]]:
                curHeight = heights[stack.pop()]
                curWidth = i - stack[-1] - 1
                res = max(res, curWidth * curHeight)
            # o.w append it
            # man, that was....gorgeous
            stack.append(i)
        return res