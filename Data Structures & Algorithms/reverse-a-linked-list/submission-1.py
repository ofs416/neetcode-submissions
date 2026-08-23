# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head
        stack = [head.val]

        link = head
        while link.next != None:
            link = link.next
            stack.append(link.val)
            

        print(stack)
        newhead = ListNode(val=stack.pop())
        current_node = newhead
        while stack:
            current_node.next = ListNode(val=stack.pop()) 
            current_node = current_node.next


        return newhead