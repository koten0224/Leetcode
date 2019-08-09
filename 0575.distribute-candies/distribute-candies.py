class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        Count=len(candies)//2

        kind=len(set(candies))
        ans=min(kind,Count)
        return ans