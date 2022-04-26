class UnionFind:
    '''
    key operations:
        find(x): Find the set containing x.
        union(x, y): Join two sets x and y.
    '''
    def __init__(self, n):
        # each node has rank and its parent
        # initially, parent is itself
        self.rank = [0] * n
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        # recursively find the 'top'
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        # A bit different in our case,
        # Since we want to check if there is a cycle
        # return True or False
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x == parent_y:
            return False # Adding the edge would lead to a cycle
        
        # Add rank on the higher rank's node
        if self.rank[parent_x] < self.rank[parent_y]:
            parent_x, parent_y = parent_y, parent_x
        self.rank[parent_x] += self.rank[parent_y]
        self.parent[parent_y] = parent_x
        return True
    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Compute distance
        dist = lambda x, y: abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])
        n = len(points)
        union_find = UnionFind(n)
        edges = list()
        # Add all edges (this case n^2)
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((dist(i, j), i, j))
        # Do not need sorting key in this case.
        edges.sort()
        # set_num to keep track of iteration steps.
        res, set_num = 0, 1
        for length, x, y in edges:
            # If adding the smallest edge does not lead to cycle
            # add.
            if union_find.union(x, y):
                res += length
                set_num += 1
                # already connected all of them, break.
                if set_num == n:
                    break
        return res

'''
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/min-cost-to-connect-all-points/solution/lian-jie-suo-you-dian-de-zui-xiao-fei-yo-kcx7/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''