# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def search(root,val):
            if root==None: return
            elif root.val==val:return root
            return search(root.left,val) or search(root.right,val)
        return search(root,val)