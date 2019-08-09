class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        li=A.split(' ')+B.split(' ')
        dic={}
        for i in li:
            if i in dic:dic[i]+=1
            else:dic[i]=1
        return [s for s in dic if dic[s]==1]