# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, None)
        prev = dummy
        currentNode1 = list1
        currentNode2 = list2

        while currentNode1 and currentNode2:
            print(currentNode1.val, currentNode2.val)
            if currentNode1 and currentNode1.val <= currentNode2.val:
                print("First list less than second list")
                prev.next = currentNode1
                currentNode1 = currentNode1.next
            else:
                print("First list greater than second list")
                prev.next = currentNode2
                currentNode2 = currentNode2.next
            prev = prev.next

        if currentNode1:
            prev.next = currentNode1
        else:
            prev.next = currentNode2
        return dummy.next
        