"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        li=[]
        if root==None:return li
        li.append(root.val)
        root=root.children
        def search(node):
            if node==None:return
            for i in node:
                li.append(i.val)
                search(i.children) 
        search(root)
        return li