'''
0057 Insert Interval
'''
'''
My method, find the leftmost overlapped interval
and the rightmost overlapped interval
Smarter way?
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        # straight forward
        # Find the location and insert?
        n = len(intervals)
        left = 0
        right = n - 1
        curMin, curMax = None, None
        while left < n:
            if intervals[left][1] < newInterval[0]:
                left += 1
            else:
                curMin = min(intervals[left][0], newInterval[0])
                break
        while right > -1:
            if intervals[right][0] > newInterval[1]:
                right -= 1
            else:
                curMax = max(intervals[right][1], newInterval[1])
                break
        if curMin is None:
            curMin = newInterval[0]
        if curMax is None:
            curMax = newInterval[1]
        return intervals[:left] + [[curMin, curMax]] + intervals[right + 1:]
            
        
'''
Simulation is a better way
Fewer iterations!
'''


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        placed = False
        ans = list()
        for li, ri in intervals:
            if li > right:
                # 在插入区间的右侧且无交集
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([li, ri])
            elif ri < left:
                # 在插入区间的左侧且无交集
                ans.append([li, ri])
            else:
                # 与插入区间有交集，计算它们的并集
                left = min(left, li)
                right = max(right, ri)
        
        if not placed:
            ans.append([left, right])
        return ans
'''
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/insert-interval/solution/cha-ru-qu-jian-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''