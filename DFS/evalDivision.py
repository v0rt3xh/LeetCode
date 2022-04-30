'''
0399 Evaluate Division
Summarize April's challenge.
A weakness: graph & corresponding algorithms & Union find
Need to review them! 
'''
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        Find a path from the starting node - ending node.
        Create a graph? But what is the weights of vertex
        Directed graph?
        Use a dictionary, dict[a], its neighbor node's result.
        Thus element would be dictionary as well
        '''
        graph = defaultdict(dict)
        # Init
        for (start_node, end_node), value in zip(equations, values):
            graph[start_node][end_node] = value
            graph[end_node][start_node] = 1.0 / value
        
        # Now define dfs helper method: (start, end)
        def dfs(start, end):
            if start not in graph or end not in graph:
                return -1
            if start == end:
                return 1
            visited.add(start)
            for neighbor in graph[start]:
                if end == neighbor:
                    return graph[start][neighbor]
                if neighbor not in visited:
                    # start the next recursive step
                    next_ans = dfs(neighbor, end)
                    # How to concatenate? Mutiply after judge != -1
                    if next_ans != -1:
                        return next_ans * graph[start][neighbor]
            return -1
        
        # 'Main method'
        result = []
        # Go through each query
        for q_start, q_end in queries:
            visited = set()
            result.append(dfs(q_start, q_end))
        return result
        
'''
Credit: @qiu-shui-zhong-de-yu
'''