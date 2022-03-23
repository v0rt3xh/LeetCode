'''
0207 Course Schedule
Directed graph.
We are trying to obtain the topological ordering 
of a acyclic directed graph.
[a, b] : b -> a / directed edge
'''
from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Creating a directed graph,
        Find its topological ordering
        The degrees of vertices matter!
        '''
        # Special case
        if len(prerequisites) == 0:
            return True
        
        # init graph
        in_degrees = [0 for _ in range(numCourses)]
        # adjacency list
        # use set to avoid repeated items
        edges = [set() for _ in range(numCourses)]
        for course1, course2 in prerequisites:
            # course2 -> course1
            # increase the degree of course1
            in_degrees[course1] += 1
            edges[course2].add(course1)
            
        # start the bfs process,
        # first load all the vertices with in-degree 0 into the stack
        queue = deque()
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)
        
        counter = 0 # use counter to give the final result
        while queue:
            vertice = queue.popleft()
            # add courses 
            counter += 1
            for neighbors in edges[vertice]:
                # check neighbors
                # minus the degree
                in_degrees[neighbors] -= 1
                # if degree = 0, okay, we can take the course
                if in_degrees[neighbors] == 0:
                    queue.append(neighbors)
        return counter == numCourses
'''
Credit：liweiwei1419 @ leetcodeCN
'''