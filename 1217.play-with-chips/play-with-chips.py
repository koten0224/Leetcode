class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        c = collections.Counter({1:0,0:0})
        c.update(i%2 for i in chips)
        return c.most_common()[-1][1]