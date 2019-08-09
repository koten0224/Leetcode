class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        st,x,count='',None,0
        for i in range(len(S)):
            if x==None and S[i]=='(':
                x=i
            if S[i]=='(':count+=1
            if S[i]==')':count-=1
            if count==0:
                st+=S[x+1:i]
                x=None
        return st