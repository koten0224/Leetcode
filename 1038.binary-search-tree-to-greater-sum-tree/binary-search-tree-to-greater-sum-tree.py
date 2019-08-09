# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def summation(node,val=0):
            if node.right:val=summation(node.right,val)
            val+=node.val
            node.val = val
            if node.left:val=summation(node.left,val)
            return val
        summation(root)
        return root