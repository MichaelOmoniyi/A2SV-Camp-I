# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        currentNode = head

        while currentNode:
            length += 1
            currentNode = currentNode.next

        partLen, extra = length // k, length % k

        currentNode = head
        parts = []
        print(partLen, extra)

        for i in range(k):
            parts.append(currentNode)

            for j in range(partLen - 1 + (1 if extra else 0)):
                if currentNode:
                    currentNode = currentNode.next
                else:
                    break

            if currentNode:
                currentNode.next, currentNode = None, currentNode.next
            extra -= (1 if extra > 0 else 0)
        return parts