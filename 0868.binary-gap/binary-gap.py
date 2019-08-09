class Solution:
    def binaryGap(self, N: int) -> int:
        sub=bin(N)
        leng=len(sub)
        index=[i for i in range(leng) if sub[i]=='1']
        leng=len(index)
        if leng==1:return 0
        gap=[index[i+1]-index[i] for i in range(leng-1)]
        ans=max(gap)
        return ans
        