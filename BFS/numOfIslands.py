'''
0200 Number of Islands
'''
'''
BFS with a lot of if clauses
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0
        queue = deque([])
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == "1":
                    count += 1
                    visited[i][j] = True
                    queue.append((i, j))
                    while queue:
                        posx, posy = queue.popleft()
                        if posx - 1 > -1 and not visited[posx - 1][posy] and grid[posx - 1][posy] == "1":
                            visited[posx - 1][posy] = True
                            queue.append((posx - 1, posy))
                        if posx + 1 < m and not visited[posx + 1][posy] and grid[posx + 1][posy] == "1":
                            visited[posx + 1][posy] = True
                            queue.append((posx + 1, posy))
                        if posy - 1 > -1 and not visited[posx][posy - 1] and grid[posx][posy - 1] == "1":
                            visited[posx][posy - 1] = True
                            queue.append((posx, posy - 1))
                        if posy + 1 < n and not visited[posx][posy + 1] and grid[posx][posy + 1] == "1":
                            visited[posx][posy + 1] = True
                            queue.append((posx, posy + 1))
        return count
                        