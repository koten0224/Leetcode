class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dic={}
        for i in A:
            if not i in dic:dic[i]=1
            else:dic[i]+=1
        for i in dic:
            if dic[i]==len(A)//2:return i
        