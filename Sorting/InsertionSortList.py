'''
0147 Insertion Sort List
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(val=float('-inf'))
        sentinel.next = head
        insertPtr = sentinel
        processPtr = head.next
        endPtr = head
        while processPtr:
            # larger than the current max, just go on
            if processPtr.val > endPtr.val:
                endPtr = processPtr
                processPtr = processPtr.next
            else:
                while insertPtr != endPtr and insertPtr.val <= processPtr.val:
                    insertPos = insertPtr
                    insertPtr = insertPtr.next
                # insertTo the correct position
                # the inserted one is the largest
                # swap
                remains = processPtr.next
                sortedNode = insertPos.next
                insertPos.next = processPtr
                processPtr.next = sortedNode
                endPtr.next = remains
                processPtr = remains
                insertPtr = sentinel
        return sentinel.next


'''
Official Solution
Neat
'''
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        dummyHead = ListNode(0)
        dummyHead.next = head
        lastSorted = head
        curr = head.next

        while curr:
            if lastSorted.val <= curr.val:
                lastSorted = lastSorted.next
            else:
                prev = dummyHead
                while prev.next.val <= curr.val:
                    prev = prev.next
                lastSorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
            curr = lastSorted.next
        
        return dummyHead.next
''''
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/insertion-sort-list/solution/dui-lian-biao-jin-xing-cha-ru-pai-xu-by-leetcode-s/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''