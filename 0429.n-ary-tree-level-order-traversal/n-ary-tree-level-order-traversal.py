"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans=[]
        def search(node,level=0):
            if node==None:return
            if level==len(ans):
                ans.append([])
            ans[level].append(node.val)
            for cnode in node.children:
                search(cnode,level+1)
        search(root)
        return ans