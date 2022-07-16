class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def removal(sequence):
            '''
            Helper method, help us remove 
            Groups of three or more consecutive balls
            '''
            number_of_removal = 1
            while number_of_removal:
                # re.subn returns the number of operations made
                sequence, number_of_removal = re.subn(r"(.)\1{2,}", "", sequence)
            return sequence
        
        hand = "".join(sorted(hand))
        
        # initialize the working queue
        # board state, hand state & number of rounds
        queue = deque([(board, hand, 0)])
        
        # visited set store the state we have traversed
        visited = {(board, hand)}
        
        while queue:
            cur_board, cur_hand, step = queue.popleft()
            for i, j in product(range(len(cur_board) + 1), range(len(cur_hand))):
                # Insert position & ball position
                if j > 0 and cur_hand[j] == cur_hand[j - 1]:
                    # Pruning Case 1:
                    # Current ball color == previous ball color, skip
                    continue
                if i > 0 and cur_board[i - 1] == cur_hand[j]:
                    # Pruning Case 2:
                    # Only place new ball before the start of consecutive same-color balls
                    continue
                
                # Only Place new ball when:
                place = False
                # Case 1: Current ball shares the same color with the following ball
                if i < len(cur_board) and cur_board[i] == cur_hand[j]:
                    place = True
                if 0 < i < len(cur_board) and cur_board[i - 1] == cur_board[i] and cur_board[i - 1] != cur_hand[j]:
                    place = True
                
                if place:
                    new_board = removal(cur_board[:i] + cur_hand[j] + cur_board[i:])
                    new_hand = cur_hand[:j] + cur_hand[j + 1:]
                    if not new_board:
                        return step + 1
                    if (new_board, new_hand) not in visited:
                        queue.append((new_board, new_hand, step + 1))
                        visited.add((new_board, new_hand))
        return -1