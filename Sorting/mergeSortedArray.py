'''
0088 Merge Sorted Array
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
            left1: the position of nums1's last element,
            left2: the position of nums2's last element,
            right: a pointer points to the insert position
        """
        left1, right = m - 1, m + n - 1
        left2 = n - 1
        # Start the merging process
        while left2 > -1 and left1 > -1:
            # nums2 is larger, okay insert it to the end
            if nums1[left1] < nums2[left2]:
                nums1[right] = nums2[left2]
                left2 -= 1
            else:
                # otherwise, just swap the zeros with nums1's element
                nums1[right], nums1[left1] = nums1[left1], nums1[right]
                left1 -= 1
            right -= 1
        # Caution, left2 may not be 0!
        while left2 > -1:
            nums1[right] = nums2[left2]
            left2 -= 1
            right -= 1