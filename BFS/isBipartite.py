'''
0785 is Bipartite?
'''
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        '''
        Basic Idea:
            Connected Set, we are painting the nodes!
            Using green and red colors.
            If the final set: painted as red / green, True
    
        Starting from the node s, we have red and green:
            paint it as red, 
            check its neighbors,
            If the neighbor node is colored, but not the same color,
            return False.
            If the neighbor node is not colored, paint it as a different color.
            Iteration ended, then True.
        NOTICE: the graph may not be connected.
        DFS or BFS
        '''
        n = len(graph)
        NOCOLOR, RED, GREEN = 0, 1, 2
        paints = [NOCOLOR] * n
        # Iterate through all the nodes
        for i in range(n):
            # Not yet painted
            if paints[i] == NOCOLOR:
                # Notice, not always connected, 
                # queue starting here
                queue = collections.deque([i])
                paints[i] == RED
                while queue:
                    node = queue.popleft()
                    current_color = GREEN if paints[node] == RED else RED
                    for neighbor in graph[node]:
                        if paints[neighbor] == NOCOLOR:
                            paints[neighbor] = current_color
                            queue.append(neighbor)
                        elif paints[neighbor] != current_color:
                            return False
        return True
