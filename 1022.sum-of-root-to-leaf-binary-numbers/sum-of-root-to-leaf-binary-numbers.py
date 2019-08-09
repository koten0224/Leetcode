# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        li=[]
        def search(node,val=''):
            val+=str(node.val)
            if not (node.left or node.right):
                li.append(val)
                return
            else:
                if node.left:search(node.left,val)
                if node.right:search(node.right,val)
        search(root)
        ans=0
        for i in li:
            ans+=int(i,2)
        return ans