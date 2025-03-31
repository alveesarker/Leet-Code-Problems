# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num_one = 0
        num_two = 0
        n_1 = l1
        n_2 = l2
        mul = 1
        while n_1 is not None or n_2 is not None:
            if n_1 is not None:
                num_one += n_1.val * mul
                n_1 = n_1.next
            if n_2 is not None:
                num_two += n_2.val * mul
                n_2 = n_2.next
            mul *= 10
        s = num_one + num_two
        temp = ListNode(s % 10)
        s //= 10
        dummy = temp
        while s > 0:
            last_dig = s % 10
            s //= 10
            new_node = ListNode(last_dig)
            dummy.next = new_node
            dummy = new_node
        return temp