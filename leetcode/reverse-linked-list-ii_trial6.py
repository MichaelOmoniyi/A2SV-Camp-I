# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        leftPrev = dummy
        currentNode = head
        count = 0

        if left == right:
            return head
        
        for _ in range(left - 1):
            print("left assignment")
            leftPrev, currentNode = currentNode, currentNode.next
            
        prev = None

        for _ in range(right - left + 1):
            nextNode = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = nextNode
        leftPrev.next.next = currentNode
        leftPrev.next = prev
        
        return dummy.next