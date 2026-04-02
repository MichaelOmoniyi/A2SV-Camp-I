# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        prev = dummy
        currentNode = head
        count = 0

        if left == right:
            return head
        
        for _ in range(left - 1):
            print("left assignment")
            prev, currentNode = currentNode, currentNode.next
        print(prev)
        leftPrev = prev
        reverseNode = currentNode
        prev = None

        for _ in range(right - left + 1):
            nextNode = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = nextNode
        leftPrev.next = prev
        reverseNode.next = currentNode
        
        return dummy.next