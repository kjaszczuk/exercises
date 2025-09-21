# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
# recursive
        # if not root:
            # return 0
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        # 7-100, 78

#iterative
        if not root:
            return 0
        max_depth = 0
        stack = [(root, 1)]

        while stack:
            # print(stack)
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return max_depth
# 100, 78
