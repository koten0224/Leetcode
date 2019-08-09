# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        li=[]
        while l1!=None:
            li.append(l1.val)
            l1=l1.next
        while l2!=None:
            li.append(l2.val)
            l2=l2.next
        li.sort()
        nodeN=node=None
        while li:
            node=ListNode(li.pop())
            node.next=nodeN
            nodeN=node
        return node