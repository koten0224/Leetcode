class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        leng = len(prices)
        for i in range(1,leng):
            profit = prices[i]-prices[i-1]
            if profit > 0 : ans += profit
        return ans