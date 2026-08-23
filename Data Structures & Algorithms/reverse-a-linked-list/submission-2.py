# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head
        if not head.next:
            return head

        new_head = self.reverseList(head.next) # new_head
        head.next.next = head      # sets the new_heads pointer to current
        head.next = None           # Deletes old link between from head to new_head
                                   # With recursion the next head points at the 'new' position
        return new_head


