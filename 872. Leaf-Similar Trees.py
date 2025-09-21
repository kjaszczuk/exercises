# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
#idziemy od lewej do prawej (ale do stosu dopisujemy najpierw prawy potem lewy, chociaz przy porownywaniu wychodzi na to samo)
# tylko gdy wezel nie ma lisci to dopisujemy go do listy, ktora bedziemy porownywac
    # optymalnie byloby przechodzic przez oba drzewa jednoczesnie, zeby jak bedzie roznica od razu zwrocic false (porownujemy listy obciete do w tym momencie krotszej)
#najpierw zrob dzialajacy przechodzacy oba w calosci jeden po drugim

# #iterative
#         stack1 = [root1]
#         stack2 = [root2]
#         leaves1 = []
#         leaves2 = []

#         while stack1:
#             node1 = stack1.pop()
#             if node1.right or node1.left:
#                 if node1.right:
#                     stack1.append(node1.right)
#                 if node1.left:
#                     stack1.append(node1.left)
#             else:
#                 leaves1.append(node1.val)

#         while stack2:
#             node2 = stack2.pop()
#             if node2.right or node2.left:
#                 if node2.right:
#                     stack2.append(node2.right)
#                 if node2.left:
#                     stack2.append(node2.left)
#             else:
#                 leaves2.append(node2.val)
#         return leaves1 == leaves2
# # 100 44

#recursive
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)
        return list(dfs(root1)) == list(dfs(root2))
# 8-100, 94
