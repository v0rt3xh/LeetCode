'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''
# Stack is the solution
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Only use one stack to maintain the left parenthe
        leftStack = []
        # Iterate through the string
        for c in s:
            if c in '([{':
                # add to the stack
                leftStack.append(c)
            # Meet right stuff, 
            # need to pop & check; CAUTION: POTENTIAL EMPTY!
            if c in '})]':
                if not leftStack:
                    return False
                matching = leftStack.pop()
                # Directly false if not match
                if matching + c not in ['()', '{}', '[]']:
                    return False
        # would be empty
        return not leftStack 