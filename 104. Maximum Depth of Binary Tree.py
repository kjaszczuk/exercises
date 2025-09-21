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
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
# 100 78
        
#iterative
        if not root:
            return 0
        max_d = 1
        depth = 1
        stack = [(root, depth)]

        while stack:
            # print(stack)
            cur = stack.pop()
            depth = cur[1]
            max_d = max(max_d, depth)
            if cur[0].left or cur[0].right:
                depth += 1
                if cur[0].left:
                    stack.append((cur[0].left, depth))
                if cur[0].right:
                    stack.append((cur[0].right, depth))
        return max_d
# 37, 29
