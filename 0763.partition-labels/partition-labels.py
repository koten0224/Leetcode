class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ans=[]
        start = 0
        for i in range(1,len(S)):
            set1 = set(S[start:i])
            set2 = set(S[i:])
            if not set1 & set2 :
                ans.append(i-start)
                start = i
        ans.append(i-start+1)
        return ans