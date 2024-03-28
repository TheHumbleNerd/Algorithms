# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        currentAncestor = root

        while currentAncestor:
            if p.val < currentAncestor.val and q.val < currentAncestor.val:
                currentAncestor = currentAncestor.left
            elif p.val > currentAncestor.val and q.val > currentAncestor.val:
                currentAncestor = currentAncestor.right
            else:
                return currentAncestor
