# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digit1 = ""
        digit2 = ""

        currentNode = l1
        while currentNode:
            digit1 = str(currentNode.val) + digit1
            currentNode = currentNode.next

        while l2:
            digit2 = str(l2.val) + digit2
            l2 = l2.next

        numAdd = int(digit1) + int(digit2)

        dummy = ListNode(-1)
        currentNode = dummy
        numAddStr = str(numAdd)[::-1]
        for i in range(len(numAddStr)):
            currentNode.next = ListNode(int(numAddStr[i]))
            currentNode = currentNode.next
        return dummy.next