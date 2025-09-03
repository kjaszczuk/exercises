# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
# recursive
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        maxl = 0; maxr = 0
        if root.left:
            maxl = self.maxDepth(root.left)+1
        if root.right:
            maxr = self.maxDepth(root.right)+1
        return max(maxl, maxr)
        # 45 78
