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
            copyMap[currentNode] = Node(currentNode.val)
            currentNode = currentNode.next

        currentNode = head
        while currentNode:
            copyMap[currentNode].next = copyMap[currentNode.next]
            copyMap[currentNode].random = copyMap[currentNode.random]
            currentNode = currentNode.next
        return copyMap[head]