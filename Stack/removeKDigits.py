'''
0402 Remove K Digits
Consider the two number 
123a456, 123b456
Order is determined by the 'first different digit'
Then, one idea is that 
We iterate through the string num, 
each time, we compare current element and the previous adjacent element, 
if current element >= adjacent elment,
    we do not drop previous element
O.W
    we drop previous element
Use a working stack.
Append element (keep)
Pop element (remove previous one)
Note: Remember to remove leading 0
'''

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        # We keep n - k elements
        keep_index = len(num) - k
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        # remove leading 0
        return "".join(stack[:keep_index]).lstrip("0") or '0'