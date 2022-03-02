'''
0022 Generate Parentheses
How to?
backtracking
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = [] # use ans to store all the possible parentheses
        def backtrack(strList, left, right):
            '''
            left: count of used (
            right: count of used )
            strList: an auxiliary list that help us store current progress 
            '''
            if len(strList) == 2 * n:
                # valid one, append
                ans.append("".join(strList))
            if left < n:
                # way 1: adding left first
                strList.append('(')
                # recur step
                backtrack(strList, left + 1, right)
                # enable backtrack
                strList.pop()
            if right < left:
                # way 2: also add right
                strList.append(')')
                backtrack(strList, left, right + 1)
                strList.pop()
        backtrack([], 0, 0)
        return ans        
                
        