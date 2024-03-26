# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        isSame = p and q and p.val == q.val
        
        if isSame:
            isSame = self.isSameTree(p.left, q.left)
        if isSame:
            isSame = self.isSameTree(p.right, q.right)
        
        return isSame
