# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        currentNode = head
        listLen = 0
        while currentNode:
            currentNode = currentNode.next
            listLen += 1

        for i in range(k % listLen):
            dummy = ListNode(-1, head)
            prev = dummy
            currentNode = prev.next

            while currentNode and currentNode.next:
                prev = currentNode
                currentNode = currentNode.next
            prev.next = None
            currentNode.next = dummy.next
            head = currentNode
        return head