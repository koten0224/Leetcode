# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        li=[]
        def search(node):
            if node==None:return
            search(node.left)
            li.append(node.val)
            search(node.right)
        search(root)
        nodeN=None
        while li:
            node=TreeNode(li.pop())
            node.right=nodeN
            nodeN=node
        return node
        