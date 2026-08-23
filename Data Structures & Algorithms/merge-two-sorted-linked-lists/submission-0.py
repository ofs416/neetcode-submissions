# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if list1 else list2

        if list1.val<list2.val:
            new_head = list1
            list1 = list1.next
        else:
            new_head = list2
            list2 = list2.next

        current_head = new_head

        while list1 or list2:
            if not list1:
                current_head.next = list2
                list2 = list2.next
            elif not list2:
                current_head.next = list1
                list1 = list1.next
            elif list1.val < list2.val:
                current_head.next = list1
                list1 = list1.next
            else:
                current_head.next = list2
                list2 = list2.next

            current_head = current_head.next

        return new_head