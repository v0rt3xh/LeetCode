'''
0023 Merge k Sorted Lists

'''

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # One by one? It's that okay?
        if not lists:
            return 
        def mergeTool(list1, list2):
            if not list1:
                return list2
            if not list2:
                return list1
            sentinel = ListNode()
            head = sentinel
            cur1, cur2 = list1, list2
            while cur1  or cur2:
                if not cur1:
                    while cur2:
                        head.next =cur2
                        cur2 = cur2.next
                        head = head.next
                    return sentinel.next
                if not cur2:
                    while cur1:
                        head.next = cur1
                        cur1 = cur1.next
                        head = head.next
                    return sentinel.next
                if cur1.val <= cur2.val:
                    head.next = cur1
                    cur1 = cur1.next
                    head = head.next
                else:
                    head.next = cur2
                    cur2 = cur2.next
                    head = head.next
            return sentinel.next
        while lists:
            if len(lists) <= 1:
                return lists[0]
            firstList = lists.pop(0)
            secondList = lists.pop(0)
            lists.append(mergeTool(firstList, secondList))