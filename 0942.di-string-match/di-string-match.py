class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        total=len(S)+1
        numlist=[i for i in range(total)]
        ans=[]
        for i in range(len(S)):
            if S[i]=='I':ans.append(numlist.pop(0))
            elif S[i]=='D':ans.append(numlist.pop())
        ans+=numlist
        return ans