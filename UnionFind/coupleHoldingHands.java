/**
0765 Couples Holding Hands
Union Find
Min Swap = # of Wrongly-seated Couples - 1
*/

class Solution {
    public int minSwapsCouples(int[] row) {
        int length = row.length;
        int N = length / 2;
        UnionFind unionfind = new UnionFind(N);
        for (int i = 0; i < length; i += 2) {
            unionfind.Union(row[i] / 2, row[i + 1] / 2);
        }
        return N - unionfind.getCount();
    }
    
    private class UnionFind {
        private int[] parent;
        
        private int count;
        
        public int getCount() {
            return count;
        }
        
        public UnionFind(int n) {
            this.count = n;
            this.parent = new int[n];
            // Init union find
            for (int i = 0; i < n; i++) {
                parent[i] = i;
            }
        }
        
        public int Find(int index) {
            while (index != parent[index]) {
                parent[index] = parent[parent[index]];
                index = parent[index];
            }
            return index;
        }
        
        public void Union(int index1, int index2) {
            int parent1 = Find(index1);
            int parent2 = Find(index2);
            if (parent1 == parent2) {
                return;
            }
            parent[parent1] = parent2;
            count--;
        }
    }
}