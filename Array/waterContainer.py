'''
0011 Container with most water
Smells familiar
two pointer 
start and end
if height[start] < height[end]:
    start += 1
else:
    end -= 1
Nothing missing? Cuz 'min' one dominate!
Check area and update.
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        area = 0
        while start < end:
            width = end - start
            if height[start] < height[end]:
                curArea = width * height[start]
                start += 1
            else:
                curArea = width * height[end]
                end -= 1
            area = max(area, curArea)
        return area
                