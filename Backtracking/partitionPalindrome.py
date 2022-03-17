'''
0131 Palindrome Partitioning
Backtrack
'''
'''
My plain solution 
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        The task: 
            1. is the substring a palindrome?
            2. Slice through the list
        '''
        def isPalin(string):
            '''
            check if a string is a palindrome,
            Here, I use the most naive way,
            we can preprocess the string and create a DP matrix
            That would be much faster! 
            '''
            n = len(string)
            if n == 1:
                return True
            left = 0
            right = n - 1
            while left <= right:
                if string[left] == string[right]:
                    left += 1
                    right -= 1
                    continue
                else:
                    return False
            return True
        '''
        2. Slicing through & backtracking steps
        '''
        def backtrack(start, end, path):
            if end >= length:
                '''
                right boundary reached
                '''
                if isPalin(s[start:end]):
                    '''
                    if the current processing unit is a palindrome
                    append it to the path, add to the resulting list
                    '''
                    path.append(s[start:end])
                    res.append(path[:])
                    # remember to pop
                    path.pop()
                return
            if isPalin(s[start:end]):
                '''
                Current one is a palindrome, either add to path
                or we keep expanding 
                (the expanding step is merged with the one outside of
                this if clause.)
                '''
                path.append(s[start:end])
                backtrack(end, end + 1, path)
                path.pop()
            backtrack(start, end + 1, path)
        res = []
        length = len(s)
        backtrack(0, 1, [])
        return res

'''
Improved Version
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        f = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]

        ret = list()
        ans = list()

        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                return
            
            for j in range(i, n):
                if f[i][j]:
                    ans.append(s[i:j+1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        return ret
'''
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/palindrome-partitioning/solution/fen-ge-hui-wen-chuan-by-leetcode-solutio-6jkv/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''