"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        li=[]
        if root==None:return li
        def search(nodes):
            if nodes==None:return
            for node in nodes:
                val=node.val
                search(node.children)
                li.append(val)
        search(root.children)
        li.append(root.val)
        return li
            