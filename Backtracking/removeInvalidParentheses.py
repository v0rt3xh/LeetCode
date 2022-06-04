'''
0301 Remove Invalid Parentheses
'''
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # First step, get rightRemove and leftRemove
        # Have a sense of how many brackets we need to remove.
        # leftRemove: number of left brackets needed
        # rightRemove: number of right brackets needed
        leftRemove, rightRemove = 0, 0
        for ch in s:
            if ch == '(':
                leftRemove += 1
            elif ch == ')':
                if leftRemove > 0:
                    leftRemove -= 1
                else:
                    rightRemove += 1
        # Create a hashset to exclude repeated solutions.
        res = set()

        def dfs(index, leftCount, rightCount, leftRemove, rightRemove, strs):
            '''
            dfs helper method Parameters:
            index: current step
            leftCount, rightCount help you determine when to add ')'
            leftRemove, rightRemove: the target number of invalid brackets.
            strs: result string tracker
            '''
            # Notice, it's possible that 
            # After traversing the string,
            # leftRemove, rightRemove are larger than 0
            if index == len(s):
                if not leftRemove and not rightRemove:
                    # Already removed all the redundant brackets.
                    res.add(strs)
                return
            # Different scenarios
            # Meet a (, and we have leftRemove > 0
            if s[index] == '(' and leftRemove:
                # Remove a '('
                dfs(index + 1, leftCount, rightCount, leftRemove - 1, rightRemove, strs)       
            # Meet a ) and we have rightRemove > 0    
            if s[index] == ')' and rightRemove:
                # Remove a ')'
                dfs(index + 1, leftCount, rightCount, leftRemove, rightRemove - 1, strs)
            # The char is a letter, add it to the result,
            # Do nothing
            if s[index] not in '()':
                 dfs(index + 1, leftCount, rightCount, 
                 leftRemove, rightRemove, strs + s[index])
                    
            # Now leftRemove is zero, no need to remove, add it.
            elif s[index] == '(':
                dfs(index + 1, leftCount + 1, rightCount, leftRemove, 
                rightRemove, strs + s[index])
            # Now s[index] == ')', when leftCount is larger than rightCount
            # We need to add ) to keep the balance.
            elif leftCount > rightCount:
                dfs(index + 1, leftCount, rightCount + 1, leftRemove, 
                rightRemove, strs + s[index])  
            # Otherwise, stop the traverse!
            return

        dfs(0, 0, 0, leftRemove, rightRemove, '')
        return list(res)           
