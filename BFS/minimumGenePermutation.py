'''
0433 Minimum Genetic Mutation
BFS approach.
'''
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # First deal with 2 special cases. 
        if start == end:
            return 0
        bank = set(bank)
        if end not in bank:
            return -1
        # Working queue, tuples as elements, current_gene, current mutations
        queue = deque([(start, 0)])
        while queue:
            current_seq, current_step = queue.popleft()
            for i, current_gene in enumerate(current_seq):
                # Iterate through all the possible mutation location
                for gene in "AGTC":
                    if gene != current_gene:
                        # Generate new sequence
                        new_gene = current_seq[:i] + gene + current_seq[i+1:]
                        # If that path possible
                        if new_gene in bank:
                            # Success 
                            if new_gene == end:
                                return current_step + 1
                            # Just like visited, we need to remove it.
                            bank.remove(new_gene)
                            queue.append((new_gene, current_step + 1))
        return -1
