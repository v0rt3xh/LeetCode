'''
1631 Path With Minimum Effort
'''
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        '''
        Consider the m * n cells as nodes in a graph.
        The distance between each consecutive nodes: abs(node_i - node_j)
        Our goal, find a route from top left to bottom right
        Such that, the maximum "distance" in the route is the smallest
        (Length of the route is the maximum "distance")   
        '''
        m, n = len(heights), len(heights[0])
        # Processing queue
        queue = [(0, 0, 0)]
        # distance array (to all the nodes, starting from 0)
        dist = [0] + [float("inf")] * (m * n - 1)
        # visited set
        visited = set()

        while queue:
            # distance, row index, col index
            # pop element from the queue (with priority)
            d, x, y = heapq.heappop(queue)
            # which node, recover the sequential number
            index = x * n + y
            if index in visited:
                # visited then continue
                continue
            if (x, y) == (m - 1, n - 1):
                # reach the end, stop
                break
            # visited current element
            visited.add(index)
            # check neighbors
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= nx < m and 0 <= ny < n and max(d, abs(heights[x][y] - heights[nx][ny])) <= dist[nx * n + ny]: # current distance is larger, update
                    dist[nx * n + ny] = max(d, abs(heights[x][y] - heights[nx][ny]))
                    heapq.heappush(queue, (dist[nx * n + ny], nx, ny))
        # return the 'effort' to the terminating node
        return dist[m * n - 1]
'''
Credit:
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/path-with-minimum-effort/solution/zui-xiao-ti-li-xiao-hao-lu-jing-by-leetc-3q2j/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''