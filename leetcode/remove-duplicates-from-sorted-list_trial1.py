# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        prev = dummy

        while head:
            if head.val == prev.val:
                prev.next = head.next
            else:
                prev = head
            head = prev.next
        return dummy.next