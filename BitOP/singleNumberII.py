'''
0137 Single Number II
Now, appear three times except one, what should you do?

Motivation:
Binary representation of all the numbers,
Since only one number appears once, others three times
the binary representation % 3 -> the number

I'm still trying to grasp the following solution
Credit: Krahets & angus123
'''

'''
For every digit in the binary form, 
it has three states: mod 3 -> {0, 1, 2}
We use binaries to represent the 3 states, (00, 01, 10)
thus we need 2 variable:
two one : 0 0 / 0 1 / 1 0 
1. How should you update two:
    if two == 0:
        if n == 0:
            one = one
        if n == 1:
            one = ~one
    if two == 1:
        one = 0

1.1 simplify for once

    if two == 0:
        one = one ^ n
    if two == 1:
        one = 0

1.2 simplify more
    one = one ^ n & ~two

2. How would you update two:
    two = two ^ n & ~one
For any digit in the binary form:
    x & 1 = x, x & 0 = 0
    x ^ 0 = x, x ^ 1 = ~x
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones
'''
作者：jyd
链接：https://leetcode-cn.com/problems/single-number-ii/solution/single-number-ii-mo-ni-san-jin-zhi-fa-by-jin407891/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''