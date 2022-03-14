'''
0150 Evaluate Reverse Polish Notation
Stack
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numstack = []
        for t in tokens:
            if t not in "+*/-":
                numstack.append(int(t))
            else:
                num2 = numstack.pop()
                num1 = numstack.pop()
                if t == '+':
                    res = num1 + num2
                elif t == '-':
                    res = num1 - num2
                elif t == '*':
                    res = num1 * num2
                elif t == '/':
                    res = abs(num1) // abs(num2)
                    if num1 * num2 < 0:
                        res *= -1
                numstack.append(res)
        return numstack[0]

'''
A solution in Python style
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_to_binary_fn = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": lambda x, y: int(x / y),   # rounding difference in python
        }

        stack = list()
        for token in tokens:
            try:
                num = int(token)
            except ValueError:
                num2 = stack.pop()
                num1 = stack.pop()
                num = op_to_binary_fn[token](num1, num2)
            finally:
                stack.append(num)
            
        return stack[0]
'''
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/solution/qiu-gen-dao-xie-zi-jie-dian-shu-zi-zhi-he-by-leetc/
来源：力扣（LeetCode）
'''