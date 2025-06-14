# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        return self.merge_sort(head)

    def merge_sort(self, head):
        if not head or not head.next :
            return head
        
        mid = self.mid(head)
        left = self.merge_sort(head)
        right = self.merge_sort(mid)

        return self.merge(left, right)
    
    def mid(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next
        
        mid = slow.next
        slow.next = None
        return mid

    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.val < right.val:
            left.next = self.merge(left.next, right)
            return left
        else:
            right.next = self.merge(left, right.next)
            return right