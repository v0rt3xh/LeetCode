'''
017 letter combinations
Recall backtracking
'''
# My solution works, but weird!
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # The dictionary for alphabets
        alphabetRef = ['abc', 'def', 'ghi', 'jkl', 'mno',
                      'pqrs', 'tuv', 'wxyz']
        res = []
        # Helper method
        def recur(prev, string):
            # the base case & return
            if string is None or len(string) == 0:
                return prev
            # compute the index reference
            button = int(string[0]) - 2
            # start dfs
            for c in alphabetRef[button]:
                newOne = recur(prev + c, string[1:])
                if newOne: # weird stuff here ...
                    res.append(newOne)
        recur('', digits)
        return res

# Different / or more formal approach:

'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        alphabetRef = ['abc', 'def', 'ghi', 'jkl', 'mno',
                      'pqrs', 'tuv', 'wxyz']
        res = []
        def recur(prev, string):
            if len(string) == 0:
                res.append(prev)
            else:
                button = int(string[0]) - 2
                for c in alphabetRef[button]:
                    newOne = recur(prev + c, string[1:])
        recur('', digits)
        return res

'''