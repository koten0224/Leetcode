class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        leng=len(S)-1
        dashList=[]
        ans=''
        for index in range(leng,-1,-1):
            sub=S[index]
            if sub.isalpha():ans+=sub
            else:dashList=[(index,sub)]+dashList
        for index,sub in dashList:
            ans=ans[:index]+sub+ans[index:]
        return ans