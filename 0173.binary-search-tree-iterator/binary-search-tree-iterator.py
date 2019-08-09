# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        def gener(node=root):
            if node.left:gener(node.left)
            self.gen.append(node.val)
            if node.right:gener(node.right)
        self.gen = []
        self.index = 0
        if root:gener()
    def next(self) -> int:
        self.index += 1
        return self.gen[self.index-1]
    def hasNext(self) -> bool:
        return self.index < len(self.gen)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()