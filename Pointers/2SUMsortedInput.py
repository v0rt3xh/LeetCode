'''
0167 Two Sum II - Input Array Is Sorted
Double pointers.
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Constant Extra Space
        '''
        n = len(numbers)
        left, right = 0, n - 1
        while left < right:
            curSum = numbers[left] + numbers[right]
            if curSum > target:
                right -= 1
            elif curSum < target:
                left += 1
            else:
                break
        return [left + 1, right + 1]