# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        result = 0
        while stack:
            node, d = stack.pop()
            if node:
                result = max(result, d)
                stack.append([node.left, 1+d])
                stack.append([node.right, 1+d])

        return result
