# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:return
        if len(nums) == 1 : return TreeNode(nums[0])
        val = max(nums)
        index = nums.index(val)
        node = TreeNode(val)
        lnums,rnums = nums[:index] , nums[index+1:]
        if lnums:node.left = self.constructMaximumBinaryTree(lnums)
        if rnums:node.right = self.constructMaximumBinaryTree(rnums)
        return node