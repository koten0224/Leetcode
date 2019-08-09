class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        leng=len(stones)
        if leng==0:return 0
        if leng==1:return stones[0]
        stones.sort(reverse=True)
        while len(stones)>1:
            x=abs(stones.pop(0)-stones.pop(0))
            if x>0:
                stones.append(x)
                stones.sort(reverse=True)
        leng=len(stones)
        if leng==0:return 0
        if leng==1:return stones[0]