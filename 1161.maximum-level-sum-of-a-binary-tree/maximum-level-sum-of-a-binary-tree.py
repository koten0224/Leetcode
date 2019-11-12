# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        node_li=[root]
        ans_li=[]
        level=1
        while node_li:
            sumation=0
            pre_node_li=[]
            for node in node_li:
                sumation+=node.val
                if node.left:
                    pre_node_li.append(node.left)
                if node.right:
                    pre_node_li.append(node.right)
            element=level,sumation
            ans_li.append(element)
            level+=1
            node_li=pre_node_li
        return max(ans_li,key=lambda x:x[1])[0]