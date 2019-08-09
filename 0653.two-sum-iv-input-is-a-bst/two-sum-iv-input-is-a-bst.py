# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def searchLeft(node):
            if node.left:yield from searchLeft(node.left)
            yield node.val
            if node.right:yield from searchLeft(node.right)
        def searchRight(node):
            if node.right:yield from searchRight(node.right)
            yield node.val
            if node.left:yield from searchRight(node.left)
        genL = searchLeft(root)
        genR = searchRight(root)
        left = next(genL)
        right = next(genR)
        while left<right:
            sun = left+right
            if sun==k:return True
            elif sun<k:left = next(genL)
            else:right = next(genR)
        return False