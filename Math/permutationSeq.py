'''
0060 Permutation Sequence
'''
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        '''
        A straight forward approach:
            We just maintain a counter,
            When the counter reach k, we return the permutation
            Exceed Runtime =D
        Need something smarter:
            I won't say I'm a genius though.
        '''
        # result string
        res = ''
        # We divide factorials all the time
        # start from n - 1, at last 0
        base = (n - 1)
        # init candidates:
        numbers = []
        # we put the numbers in an ascending order
        for i in range(n):
            numbers.append(str(i + 1))
        # k minus 1 makes corner cases a lot EASIER!
        k -= 1
        # the last step, always end at 0! (zero factorial)
        while base  >= 0:
            # get the "order", pick that number
            order = k // math.factorial(base)
            # catenate the number
            res = res + numbers[order]
            # update number list
            numbers = numbers[:order] + numbers[order + 1:]
            # make k smaller
            k -= order * math.factorial(base)
            # reduce base as well
            base -= 1
        return res