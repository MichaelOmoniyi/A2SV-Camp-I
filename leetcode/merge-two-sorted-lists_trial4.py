# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive function
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            currentNode = list1
            currentNode.next = self.mergeTwoLists(list1.next, list2)
            return currentNode
        else:
            currentNode = list2
            currentNode.next = self.mergeTwoLists(list1, list2.next)
            return currentNode
        # dummy = ListNode(-1, None)
        # prev = dummy
        # currentNode1 = list1
        # currentNode2 = list2

        # while currentNode1 and currentNode2:
        #     if currentNode1 and currentNode1.val <= currentNode2.val:
        #         prev.next = currentNode1
        #         currentNode1 = currentNode1.next
        #     else:
        #         prev.next = currentNode2
        #         currentNode2 = currentNode2.next
        #     prev = prev.next

        # if currentNode1:
        #     prev.next = currentNode1
        # else:
        #     prev.next = currentNode2
        # return dummy.next
        