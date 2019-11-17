# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        
        def tree_sum(node,sumation=0):
            if not node:return sumation
            sumation=tree_sum(node.right,sumation=sumation)
            node.val=sumation=sumation+node.val
            sumation=tree_sum(node.left,sumation=sumation)
            return sumation
        tree_sum(root)
        return root