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

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subRoot:
            return False
        if not root and not subRoot:
            return True
        
        isSubTree = self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        return isSubTree
