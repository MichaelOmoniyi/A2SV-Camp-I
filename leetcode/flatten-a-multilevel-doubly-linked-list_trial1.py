"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        currentNode = head
        stack = []

        while currentNode:
            if currentNode.child:
                if currentNode.next:
                    stack.append(currentNode.next)
                currentNode.next, currentNode.child.prev= currentNode.child, currentNode
                currentNode.child = None
            
            if currentNode.next == None and stack:
                rightNode = stack.pop()
                currentNode.next, rightNode.prev = rightNode, currentNode
            currentNode = currentNode.next
        return head