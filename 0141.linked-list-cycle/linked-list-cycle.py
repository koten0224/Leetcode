# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        li=set()
        count=0
        while head:
            if head.val in li:count+=1
            else:count=0
            if count>=6:return True
            li.add(head.val)
            head=head.next
        return False
        