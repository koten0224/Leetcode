class Solution:
    def removeDuplicates(self, S: str) -> str:
        i=0
        leng=len(S)-1
        while i<leng:

            if S[i]==S[i+1]:
                S=S[:i]+S[i+2:]
                leng-=2
                if i:i-=1
            else:i+=1
        return S