# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(None)
        partitionNode = ListNode(None)

        currentNode = head
        prePartition = dummy
        afterPartition = partitionNode
        while currentNode:
            if currentNode.val < x:
                prePartition.next = currentNode
                prePartition = currentNode
            elif currentNode.val >= x:
                afterPartition.next = currentNode
                afterPartition = currentNode
            currentNode = currentNode.next
        afterPartition.next = None
        prePartition.next = partitionNode.next
        return dummy.next