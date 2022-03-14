'''
0148 Sort List
Merge sort with some adaptations
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def findMid(start, end):
            '''
            Helper method to find the mid node
            '''
            slow = start
            fast = start.next
            while fast != end and fast.next != end:
                fast = fast.next.next
                slow = slow.next
            return slow
        def mergeSort(start, end):
            '''
            Merge sort step
            '''
            if start == end:
                '''
                Only one node, just return
                '''
                return start
        
            mid = findMid(start, end)
            # break the connections here
            # but, do we really need this?
            # we can improve the whole structure 
            #(like the official solution)
            midNext = mid.next
            mid.next = None
            # recursive step
            sorted1 = mergeSort(start, mid)
            sorted2 = mergeSort(midNext, end)
            merged = merge(sorted1, sorted2)
            return merged
        def merge(head1, head2):
            sentinel = ListNode()
            cur = sentinel
            cur1, cur2 = head1, head2
            while cur1 or cur2:
                if not cur1:
                    cur.next = cur2
                    break
                if not cur2:
                    cur.next = cur1
                    break
                if cur1 and cur2:
                    if cur1.val <= cur2.val:
                        # Do you have to shift it to None
                        # And use tmp?
                        tmp = cur1.next
                        cur1.next = None
                        cur.next = cur1
                        cur1 = tmp
                    else:
                        tmp = cur2.next
                        cur2.next = None
                        cur.next = cur2
                        cur2 = tmp
                    cur = cur.next
            return sentinel.next
        return mergeSort(head, None)

'''
bottom-top approach: 
    get the length first, works like a queue
'''

'''
Improved top-bottom approach
'''
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def sortFunc(head: ListNode, tail: ListNode) -> ListNode:
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return merge(sortFunc(head, mid), sortFunc(mid, tail))
            
        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next
        
        return sortFunc(head, None)
'''
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/sort-list/solution/pai-xu-lian-biao-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''