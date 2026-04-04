# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        listLen = 1
        tail = head

        while tail.next:
            tail = tail.next
            listLen += 1
        print(f"list length: {listLen}")

        k = k % listLen
        if k == 0:
            return head

        currentNode = head
        for i in range(listLen - k - 1):
            currentNode = currentNode.next

        newHead = currentNode.next
        currentNode.next = None
        tail.next = head
        return newHead