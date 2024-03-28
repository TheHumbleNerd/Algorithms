# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodesHelper(self, node: TreeNode, maxVal: int, result: List[int]):
        if not node:
            return
        if node.val >= maxVal:
            result[0] += 1
        maxVal = max(maxVal, node.val)
        self.goodNodesHelper(node.left, maxVal, result)
        self.goodNodesHelper(node.right, maxVal, result)

    def goodNodes(self, root: TreeNode) -> int:
        result = [0]
        maxVal = root.val
        self.goodNodesHelper(root, maxVal, result)
        return result[0]
