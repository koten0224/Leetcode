# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        currNode = node
        while currNode.next is not None:
            currNode.val = currNode.next.val
            prevNode = currNode
            currNode = currNode.next

        prevNode.next = None