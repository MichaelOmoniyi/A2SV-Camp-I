"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyMap = {None: None}

        currentNode = head
        while currentNode:
            copyNode = Node(currentNode.val)
            copyMap[currentNode] = copyNode
            currentNode = currentNode.next

        currentNode = head
        while currentNode:
            copyNode = copyMap[currentNode]
            copyNode.next = copyMap[currentNode.next]
            copyNode.random = copyMap[currentNode.random]
            currentNode = currentNode.next
        return copyMap[head]