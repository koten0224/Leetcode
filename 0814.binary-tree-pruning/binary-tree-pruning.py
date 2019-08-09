# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        def foo(node):
            
            left=right=0
            if node.left:left=foo(node.left)
            if node.right:right=foo(node.right)
            if not left:node.left=None
            if not right:node.right=None
            val=node.val+left+right
            return val
        
        if root:foo(root)
        return root