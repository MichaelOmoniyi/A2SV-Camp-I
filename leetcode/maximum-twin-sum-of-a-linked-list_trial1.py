# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev = None
        currentNode = head
        while currentNode:
            newNode = ListNode(currentNode.val)
            nextNode = currentNode.next
            newNode.next, prev = prev, newNode
            currentNode = nextNode

        currentNode, twinNode = head, prev
        twinSum = 0
        while currentNode:
            twinSum = max(twinSum, currentNode.val + twinNode.val)
            currentNode = currentNode.next
            twinNode = twinNode.next
        return twinSum
        