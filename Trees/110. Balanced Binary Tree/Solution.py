# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # does not necessarily return the right height,
    # since the code is optimized for returning the correct balancing info as soon as possible
    def balanceCheckHelper(self, root: Optional[TreeNode]) -> [bool, int]:
        if not root:
            return [True, 0]
        
        lBalanced, rBalanced = [False, False]
        lHeight, rHeight = 0, 0
        lBalanced, lHeight = self.balanceCheckHelper(root.left)

        if lBalanced:
            rBalanced, rHeight = self.balanceCheckHelper(root.right)

        isBalanced = lBalanced and rBalanced
        if isBalanced and abs(lHeight - rHeight) > 1:
            isBalanced = False
        
        return [isBalanced, 1 + max(lHeight, rHeight)]

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = self.balanceCheckHelper(root)

        return result[0]
