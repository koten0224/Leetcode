# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        li=[]
        while head:
            li.append(head.val)
            head=head.next
        li=li[len(li)//2:]
        nodeN=None
        while li:
            node=ListNode(li.pop())
            node.next=nodeN
            nodeN=node
        return node