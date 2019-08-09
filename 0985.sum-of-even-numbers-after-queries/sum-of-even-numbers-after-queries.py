class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        ansval=sum([i for i in A if not i%2])
        for v,i in queries:
            val=A[i]
            if val%2:
                if v%2:ansval+=val+v
            else:
                if v%2:ansval-=val
                else:ansval+=v
            A[i]+=v
            ans.append(ansval)
        return ans