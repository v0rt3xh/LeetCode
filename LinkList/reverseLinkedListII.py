'''
0092 Reverse Linked List II
A must-have!
We will study it thoroughly
'''
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverse_linked_list(head: ListNode):
            # Helper method to reverse a linked list (starting from head)
            pre = None
            cur = head
            while cur:
                nex = cur.next
                cur.next = pre
                pre = cur
                cur = nex

        # sentinel trick
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node
        # we find the node before 'starting index'
        for _ in range(left - 1):
            pre = pre.next
        # find the node at the 'ending index'
        right_node = pre
        for _ in range(right - left + 1):
            right_node = right_node.next
        # Cut a sub linked list from the original one
        left_node = pre.next # the start
        curr = right_node.next # remaining part
        
        # break previous links
        pre.next = None
        right_node.next = None

        # use the reverse method
        reverse_linked_list(left_node)
        # catenate back
        pre.next = right_node
        left_node.next = curr
        return dummy_node.next

'''
Even better approach, insert from the front!
e.g. 1 - 2 - 3 - 4, start from 2, end at 4
     1 - 3 - 2 - 4
     1 - 4 - 3 - 2
'''

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # sentinel trick as always
        dummy_node = ListNode(-1)
        dummy_node.next = head
        # pre serve as a cursor
        pre = dummy_node
        # let the node points to the left boundary 
        # (not in the left - right range)
        for _ in range(left - 1):
            pre = pre.next
        '''
        cur: points to starting position of 'reverse sequence'
        pre: points to the left boundary
        next: the element that we insert to the front
        '''
        cur = pre.next
        # iteration takes right - left many iterations
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        return dummy_node.next
'''
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii/solution/fan-zhuan-lian-biao-ii-by-leetcode-solut-teyq/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''