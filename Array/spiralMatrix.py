'''
0054 Spiral Matrix
simulation,
Though my if / else controller looks not that cool
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # right
        # down
        # left 
        # up
        res = []
        m, n = len(matrix), len(matrix[0])
        right, left, up, down = n - 1, 0, 0, m - 1
        while right >= left and up <= down :
            for i in range(left, right + 1):
                res.append(matrix[up][i])
            up += 1
            if up > down: break
            for j in range(up, down + 1):
                res.append(matrix[j][right])
            right -= 1
            if right < left: break
            for k in range(right, left - 1, -1):
                res.append(matrix[down][k])
            down -= 1
            if down < up: break
            for l in range(down, up - 1, -1):
                res.append(matrix[l][left])
            left += 1
        return res

