class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        flagABig = False
        i = 0
        j = 0
        if sum(A)>sum(B):
            flagABig = True
        if flagABig:
            diff = (sum(A)-sum(B))/2
            A = set(map(lambda x: x - diff, A))
            B = set(B)
            val = (A&B).pop()
            return [val+diff,val]
        else:
            diff = (sum(B)-sum(A))/2
            A = set(A)
            B = set(map(lambda x: x - diff, B))
            val = (A&B).pop()
            return [val,val+diff]