# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def validBSTHelper(self, root: Optional[TreeNode], minVal:int, maxVal: int) -> bool:
        if not root:
            return True
        
        if root.val <= minVal or root.val >= maxVal:
            return False
        
        isLeftBST = self.validBSTHelper(root.left, minVal, root.val)
        isRightBST = self.validBSTHelper(root.right, root.val, maxVal)

        return isLeftBST and isRightBST

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minVal = float('-inf')
        maxVal = float('inf')
        return self.validBSTHelper(root, minVal, maxVal)
