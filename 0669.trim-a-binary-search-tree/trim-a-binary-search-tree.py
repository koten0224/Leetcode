# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        def trim(node):
            if node and node.left:node.left=trim(node.left)
            if node and node.right:node.right=trim(node.right)
            while node and (node.val<L or R<node.val):
                if node.left:node=node.left
                else:node=node.right
            return node    
        root=trim(root)
        return root