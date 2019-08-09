# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if not N%2 : return []
        root = TreeNode(0)
        if N==1:return [root]
        if N==3:
            root.left = TreeNode(0)
            root.right = TreeNode(0)
            return [root]
        ans = []
        def foo(a,b):
            root = TreeNode(0)
            root.left = a
            root.right = b
            ans.append(root)
        for num1 in range(1,N//2+1,2):
            num2 = N-num1-1
            nodes1 = self.allPossibleFBT(num1)
            nodes2 = self.allPossibleFBT(num2)
            for node1,node2 in itertools.product(nodes1,nodes2):
                foo(node1,node2)
                if num1 != num2:foo(node2,node1)
        return ans