# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Solution 1
        # maxDepth = 0

        # def depthFirstSearch(root, depth):
        #     nonlocal maxDepth

        #     if not root:
        #         return None

        #     maxDepth = max(maxDepth, depth)
        #     depthFirstSearch(root.left, depth + 1)
        #     depthFirstSearch(root.right, depth + 1)
        # depthFirstSearch(root, 1)
        # return maxDepth

        # Solution 2
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)