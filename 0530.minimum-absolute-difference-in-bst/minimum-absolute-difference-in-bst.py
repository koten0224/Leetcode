# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        li=set()
        def search(node):
            if not node:return
            li.add(node.val)
            search(node.left)
            search(node.right)
        search(root)
        ans=2**31
        temp=sorted(li)
        pre=temp[0]
        print(temp)
        for i in temp[1:]:
            pre_ans=i-pre
            if pre_ans<ans:ans=pre_ans
            pre=i
        return ans
            