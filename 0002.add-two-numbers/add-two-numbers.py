# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        int1=int2=''
        while l1!=None:
            int1=str(l1.val)+int1
            l1=l1.next
        while l2!=None:
            int2=str(l2.val)+int2
            l2=l2.next
        sum_=str(int(int1)+int(int2))
        outputN=None
        while sum_:
            output=ListNode(int(sum_[0]))
            output.next=outputN
            outputN=output
            sum_=sum_[1:]
        return output