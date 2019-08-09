"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root==None:return 0
        if root.children==[]:return 1
        levellist=[]
        def search(root,level=2):
            if not root and root!=0:return
            levellist.append(level)
            for i in root:
                search(i.children,level+1)
        search(root.children)
        return max(levellist)