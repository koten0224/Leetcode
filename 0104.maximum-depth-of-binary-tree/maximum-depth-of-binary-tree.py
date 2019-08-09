# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:return 0
        
        levellist=[]
        def search(node,level=1):
            if not node and node!=0:return
            levellist.append(level)

            search(node.left,level+1)  
            search(node.right,level+1)
        search(root)
        return max(levellist)