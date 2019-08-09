# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dic={}
        while head:
            dic[head.val]=1
            head=head.next
        li=[i for i in dic]
        li.sort()
        node=nodeN=None
        while li:
            node=ListNode(li.pop())
            node.next=nodeN
            nodeN=node
        return node
        