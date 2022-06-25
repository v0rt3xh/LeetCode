'''
0417 Pacific Atlantic Water Flow
BFS / DFS:
A good approach for determining 'reach both oceans'
Start from the left / top boundaries, reversely search,
determine which cells can flow to Pacific;
Start from the right / bottom boundaries, search reversely,
determine which cells can flow to Atlantic.
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        
        def bfs(starting_positions):
            '''
            starting_positions is a list of cell coordinate
            '''
            working_queue = collections.deque(starting_positions)
            visited = set(starting_positions)
            while working_queue:
                x, y = working_queue.popleft()
                for next_x, next_y in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if -1 < next_x < m and -1 < next_y < n and heights[x][y] <= heights[next_x][next_y] and (next_x, next_y) not in visited:
                        visited.add((next_x, next_y))
                        working_queue.append((next_x, next_y))
            return visited
        
        # Avoid adding duplicate coordinates into boundary list.
        pacific_boundary = [(i, 0) for i in range(m)] + [(0, j) for j in range(1, n)]
        atlantic_boundary = [(m - 1, i) for i in range(n)] + [(j, n - 1) for j in range(m - 1)]
        # Get the intersection of set,
        # convert the tuples into lists.
        return list(map(list, bfs(pacific_boundary) & bfs(atlantic_boundary)))
                    
                
            