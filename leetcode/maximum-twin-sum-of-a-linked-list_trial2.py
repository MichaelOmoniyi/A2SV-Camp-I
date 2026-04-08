# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        currentNode = slow
        while currentNode:
            newNode = ListNode(currentNode.val)
            nextNode = currentNode.next
            newNode.next, prev = prev, newNode
            currentNode = nextNode

        currentNode, twinNode = head, prev
        twinSum = 0
        while twinNode:
            twinSum = max(twinSum, currentNode.val + twinNode.val)
            currentNode = currentNode.next
            twinNode = twinNode.next
        return twinSum
        