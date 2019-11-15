# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode,left=False,sumation=0) -> int:
        if not root:return sumation
        if left and not(root.left or root.right):
            sumation+=root.val
        else:
            sumation=self.sumOfLeftLeaves(root.left,left=True,sumation=sumation)
            sumation=self.sumOfLeftLeaves(root.right,left=False,sumation=sumation)
        return sumation