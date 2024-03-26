# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterHelper(self, result: List[int], root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        lHeight = self.diameterHelper(result, root.left)
        rHeight = self.diameterHelper(result, root.right)

        currentDiameter = 0
        if lHeight > 0 and rHeight > 0:
            currentDiameter = lHeight + rHeight
        elif lHeight > 0:
            currentDiameter = lHeight
        elif rHeight > 0:
            currentDiameter = rHeight
        result[0] = max(result[0], currentDiameter)

        return 1 + max(lHeight, rHeight)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = [0]
        self.diameterHelper(result, root)

        return result[0]
