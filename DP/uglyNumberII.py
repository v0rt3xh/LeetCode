'''
0264 Ugly Number II
DP idea & pointers.
'''
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        DP = [0] * (n + 1)
        DP[1] = 1
        p2 = p3 = p5 = 1
        for i in range(2, n + 1):
            two = DP[p2] * 2
            three = DP[p3] * 3
            five = DP[p5] * 5
            DP[i] = min(two, three, five)
            if (DP[i] == two):
                p2 += 1
            if (DP[i] == three):
                p3 += 1
            if (DP[i] == five):
                p5 += 1
        return DP[n]