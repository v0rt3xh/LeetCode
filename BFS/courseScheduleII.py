'''
0210 Course Schedule II
By the way, I should move Course Schedule I 
to the BFS folder as well. :)
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Similar logic as Course Schedule I, right?
        if len(prerequisites) == 0:
            return [i for i in range(numCourses)]
        # init, build the graph, 
        # assign degrees to each node
        degrees = [0 for _ in range(numCourses)]
        adjacency = [set() for _ in range(numCourses)]
        res = list()
        # cur: current course
        # pre: preliminary course
        for cur_course, pre_course in prerequisites:
            degrees[cur_course] += 1
            adjacency[pre_course].add(cur_course)
        # init finished, now start BFS procedure
        queue = collections.deque()
        for i in range(numCourses):
            if degrees[i] == 0:
                queue.append(i)
        while queue:
            vertex = queue.popleft()
            res.append(vertex)
            for neighbor in adjacency[vertex]:
                # reduce the degree of neighbor
                # cuz we have finish one preliminary course!
                degrees[neighbor] -= 1
                if degrees[neighbor] == 0:
                    queue.append(neighbor)
        if len(res) == numCourses:
            return res
        return []