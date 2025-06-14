# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_node_list = None

        while head:
            next_node = head.next 
            head.next = new_node_list
            new_node_list = head
            head = next_node

        return new_node_list
            
        