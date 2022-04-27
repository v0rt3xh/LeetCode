'''
1202 Smallest String With Swaps
'''
class UnionFind():
    '''
    Yesterday's code :)
    '''
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x == parent_y:
            return
        if self.rank[parent_x] < self.rank[parent_y]:
            parent_x, parent_y = parent_y, parent_x
        self.rank[parent_x] += self.rank[parent_y]
        self.parent[parent_y] = parent_x

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        '''
        Union find?
        All the subgrph should be smallest -> overall smallest
        Greedy proof
        '''
        union_find = UnionFind(len(s))
        for x, y in pairs:
            union_find.union(x, y)
            
        # Then, critical step, use union find
        # Each set, contains what characters?
        character_dict = collections.defaultdict(list)
        
        # notice we build the set based on index (0, 1, ... n - 1)
        for idx, c in enumerate(s):
            character_dict[union_find.find(idx)].append(c)
        
        # Okay, got the set & characters, sort them!
        for sets in character_dict.values():
            sets.sort(reverse=True)
            
        # Final step, concatenate
        res = list()
        # start from index 0 
        # search its parent node
        # append the last element in the list
        # avoid pop from front, for efficiency
        for i in range(len(s)):
            parent = union_find.find(i)
            res.append(character_dict[parent][-1])
            character_dict[parent].pop()
        return ''.join(res)