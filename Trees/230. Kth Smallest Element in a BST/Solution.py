# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st = []
        count = 0
        node = root

        while node or st:
            while node:
                st.append(node)
                node = node.left
            
            node = st.pop()

            count += 1
            if count == k:
                return node.val

            node = node.right
