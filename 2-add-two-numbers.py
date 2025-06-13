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
        head = ListNode(0)
        current = head
        rest = head.val

        while l1 or l2 or rest:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            val_sum = val1 + val2 + rest
            digit = val_sum % 10
            rest = val_sum // 10

            current.next = ListNode(digit)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next