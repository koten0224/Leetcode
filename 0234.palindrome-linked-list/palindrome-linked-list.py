# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        li=[]
        while head:
            li.append(head.val)
            head=head.next
        leng=len(li)
        if leng<2:return True
        if leng==2:return li[0]==li[1]
        li1,li2=li[:len(li)//2+leng%2],li[len(li)//2:]
        li2.reverse()
        return li1==li2