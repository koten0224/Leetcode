# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        li=set()
        def search(node):
            if node==None:return
            li.add(node.val)
            search(node.left)
            search(node.right)
        search(root)
        return len(li)==1