# maintain two pointers?
# Also need to store '1'
# null case?
'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''
# Well, the reasoning seems to be straight-forward
# traverse through the 2 linked list
# take care of add 1, you may neglect it!
# There are some tricky stuff however

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sentinel = ListNode() # Sentinel trick
        ptr1 = l1 
        ptr2 = l2
        # Keep a current cursor, which helps us add on the result list.
        current = sentinel
        digit = 0
        # Each traversal, what are we doing?
        # Any digit left? In case left out at the top
        # ptr1 has stuff
        # ptr2 has stuff
        while digit or ptr1 or ptr2:
            curVal = digit # Magic! ensure that we will handle left 1 case
            if ptr1: # ptr2 treated as 0
                curVal += ptr1.val
                ptr1 = ptr1.next
            if ptr2: # ptr1 treated as 0 
                curVal += ptr2.val
                ptr2 = ptr2.next
            current.next = ListNode(curVal % 10)
    
            current = current.next
            digit = curVal // 10
            
        return sentinel.next