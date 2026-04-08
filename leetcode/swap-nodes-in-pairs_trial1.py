# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(None, head)
        prev, currentNode = dummy, dummy.next
        while currentNode and currentNode.next:
            nextNode = currentNode.next.next
            secondNode = currentNode.next

            secondNode.next = currentNode
            currentNode.next = nextNode
            prev.next = secondNode

            prev, currentNode = currentNode, nextNode
        return dummy.next