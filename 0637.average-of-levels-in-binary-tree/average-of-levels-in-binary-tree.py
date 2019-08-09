# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans=[]
        def search(node,level=0):
            if node==None:return
            if level==len(ans):ans.append([])
            ans[level].append(node.val)
            search(node.left,level+1)
            search(node.right,level+1)
        search(root)

        return [sum(re)/len(re) for re in ans]