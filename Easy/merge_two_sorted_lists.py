# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        dummy = ListNode(-1)
        current = dummy
        n1 = list1
        n2 = list2
        while n1 is not None and n2 is not None:
            if n1.val > n2.val:
                current.next = n2
                n2 = n2.next
                current = current.next
            else:
                current.next = n1
                n1 = n1.next
                current = current.next
        if n1 is None:
            current.next = n2
        elif n2 is None:
            current.next = n1
        return dummy.next
        