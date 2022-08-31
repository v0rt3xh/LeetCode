'''
0436 Find Right Interval
Notice that each left end is unique. 
We can utilize two arrays.
Each sorted in ascending order. 
- Left End
- Right End
For the i-th element in Right End,
if its right interval is the j-th element in Left End,
For the i + 1-th element in Right End,
we only need to start our search from j-th element. 
'''

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        num_element = len(intervals)
        # Get separate list for left/right ends.
        leftEnds, rightEnds = list(zip(*intervals))
        # Append the index and sort
        leftEnds = sorted(zip(leftEnds, range(num_element)))
        rightEnds = sorted(zip(rightEnds, range(num_element)))
        result = [-1] * num_element
        j = 0
        # Actually an implicit two pointers approach.
        for end, index in rightEnds:
            while j < num_element and leftEnds[j][0] < end:
                j += 1
            if j < num_element:
                result[index] = leftEnds[j][1]
        return result