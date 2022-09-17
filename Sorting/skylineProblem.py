'''
0218 The Skyline Problem
Priority Queue
'''

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # By default, python's heapq is a min-heap.
        # Thus, we want a reverse height value.
        events = [(left, -height, right) for left, right, height in buildings]
        # Also need to consider the bottom right ends. 
        events += [(right, 0, 0) for _, right, _ in buildings]
        events.sort()
        # Neat initialization
        res = [[0, 0]] 
        queue = [(0, float('inf'))]
        for left, minusH, right in events:
            # restore height
            height = -minusH
            while left >= queue[0][1]:
                # outside of scope, pop
                heapq.heappop(queue)
            if height: 
                # not 0, should be considered
                # still negative height
                heapq.heappush(queue, (-height, right))
            # Check the previous point's height
            if res[-1][1] != -queue[0][0]:
                # Not the same, then append.
                res.append([left, -queue[0][0]])
        return res[1:]