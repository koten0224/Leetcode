class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=None
        ans=0
        for i in prices:
            if buy==None or i<buy:
                buy=i
            elif i>buy:
                earn = i-buy
                if earn>ans:
                    ans=earn
        return ans
                