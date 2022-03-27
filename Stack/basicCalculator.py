'''
0224 Basic Calculator
'''
class Solution:
    def calculate(self, s: str) -> int:
        '''
        We only need to compute + or -
        Thus, removing parentheses may not be a big deal,
        we just need to care about shifting the signs!
        -(1 + 2) == -1 - 2
        i.e, when we meet a parenthesis starting with - => -(
        the sign after it should be flipped
        '''
        ops = [1]
        sign = 1 # keeps current sign

        ret = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                # meet +, the sign is the same as top element in ops
                sign = ops[-1]
                i += 1
            elif s[i] == '-':
                # meet -, flip
                sign = -ops[-1]
                i += 1
                # meet (, append the sign
            elif s[i] == '(':
                ops.append(sign)
                i += 1
            elif s[i] == ')':
                # meet ), pop the sign
                ops.pop()
                i += 1
            else:
                # add / minus the number to result
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + ord(s[i]) - ord('0')
                    i += 1
                # according to the current sign
                ret += num * sign
        return ret
'''
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/basic-calculator/solution/ji-ben-ji-suan-qi-by-leetcode-solution-jvir/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''        