'''
0202 Happy Number
'''
'''
Hashset, not fast enough.
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            res = 0
            visited.add(n)
            while n:
                res += (n % 10) ** 2
                n //= 10
            n = res
        return 1 in visited

'''
Linked List Cycle! 
Intrinsic Linked list
detect if there is a cycle.
'''
class Solution:
    def isHappy(self, n: int) -> bool: 
        # node = node.next
        # How to get next 
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        # fast, slow pointer
        slow_runner = n
        fast_runner = get_next(n)
        # fast may meet 1, or there would be a cycle.
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            # slow move 1 step
            # fast move 2 steps
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1
'''
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/happy-number/solution/kuai-le-shu-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''