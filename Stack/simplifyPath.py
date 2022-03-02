'''
0071 Simplify Path

stack
'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        # split the folder names by '/'
        folders = path.split('/')
        # use a stack to store those folder names
        stack = []

        for folder in folders:
            # '..' correspond to the parent folder!
            if folder == '..':
                if stack: # if the stack if none empty, pop out the parent folder
                    stack.pop()
            elif folder and folder != '.':
                # otherwise, current folder has a name & not refer to current folder
                # append it to the stack
                stack.append(folder)
        # remember to add the root '/'
        return '/' + '/'.join(stack)