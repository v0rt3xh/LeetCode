'''
0215 k-th Largest Element
Quick sort, partition the pivot to the n-k th position.
Good review of quicksort
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def findTopKth(low, high):
            # Get a random pivot
            pivot = random.randint(low, high)
            # swap the pivot to the left 
            nums[low], nums[pivot] = nums[pivot], nums[low]
            # record the pivot value
            base = nums[low]
            i = low # serve as a marker for inserting position
            j = low + 1 # cursor
            while j <= high:
                if nums[j] > base: # element larger than pivot value
                    # swap with the (i + 1)
                    # pivot, (numbers larger than it), (numbers larger than it)
                    nums[i + 1], nums[j] = nums[j], nums[i + 1]
                    i += 1
                j += 1
            # swap the pivot with the rightmost value that >= its value.
            nums[low], nums[i] = nums[i], nums[low]
            # (Descending order)
            if i == k - 1:
                # return
                return nums[i]
            elif i > k - 1:
                # partition left half
                return findTopKth(low, i - 1)
            else:
                # partition right half
                return findTopKth(i + 1, high)
        return findTopKth(0, len(nums) - 1)

'''
Credit: 郁郁雨 @ leetcode-cn
'''