# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def getLeaf(root,List=List):
            if root==None:return True
            left=getLeaf(root.left,List)
            right=getLeaf(root.right,List)
            if left and right:List.append(root.val)
            
        List1=[]
        List2=[]
        getLeaf(root1,List1)
        getLeaf(root2,List2)
        return List1==List2