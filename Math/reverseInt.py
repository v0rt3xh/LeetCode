'''
0007 reverse integer
What kind of method?
# If not handling overflow, ez
# handling overflow??
'''
class Solution:
    def reverse(self, x: int) -> int:
        tmp = 1
        if x < 0:
            tmp = -1
            x = -x
        prev = 0
        res = 0
        while x:
            res = 10 * res + (x % 10)
            x //= 10
        if res > 2 ** 31 - 1 or -res < -2 ** 31:
            return 0
        return tmp * res


'''
class Solution {
    public int reverse(int x) {
        int ans = 0;
        while (x != 0) {
            int pop = x % 10;
            if (ans > Integer.MAX_VALUE / 10 || (ans == Integer.MAX_VALUE / 10 && pop > 7)) 
                return 0;
            if (ans < Integer.MIN_VALUE / 10 || (ans == Integer.MIN_VALUE / 10 && pop < -8)) 
                return 0;
            ans = ans * 10 + pop;
            x /= 10;
        }
        return ans;
    }
}

作者：guanpengchn
链接：https://leetcode-cn.com/problems/reverse-integer/solution/hua-jie-suan-fa-7-zheng-shu-fan-zhuan-by-guanpengc/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''