'''
0056 Merge Intervals

'''
# First attempt, quite straight forward, but the performance is poor.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # We first need to sort the intervals,
        # Sort by what? the first value in the list
        intervals.sort(key=lambda x:x[0])
        res = []
        cursor = 0
        # Iterative steps:
        # Merge current interval with all possible overlaps
        while cursor < len(intervals):
            if cursor + 1 >= len(intervals):
                res.append(intervals[cursor])
                break
            left1, right1 = intervals[cursor]
            left2, right2 = intervals[cursor + 1]
            if right1 >= left2: # There are some overlapping
                cursor += 1
                intervals[cursor] = [left1, max(right1, right2)]
            else:
                cursor += 1
                res.append(intervals[cursor])
        return res 