class Solution(object):
    def shortestToChar(self, S, C):
        C_index=[]
        leng=len(S)
        for i in range(leng):
            if S[i]==C:C_index.append(i)
            
        ans=[min([abs(i-j) for j in C_index]) for i in range(len(S))]
        return ans