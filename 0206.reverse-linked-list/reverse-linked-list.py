# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        li=[]
        if head==None:return None
        while head:
            li.append(head.val)
            head=head.next
        nodeN=None
        while li:
            node=ListNode(li.pop(0))
            node.next=nodeN
            nodeN=node
        return node
        