'''
0817 Linked List Components
Use nums as a hash set,
we traverse through the linked list,
once we observe that:
- Current val is in the set,
- but the next val is not in the set,
- We can increase connected components by 1.
'''
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        num_set = set(nums)
        cursor = head
        result = 0
        while cursor:
            if (cursor.val in num_set and 
               getattr(cursor.next, 'val', None) not in num_set):
                result += 1
            cursor = cursor.next
        return result