class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        leng = len(costs)
        halfLeng = leng//2
        costs.sort(key=lambda x:x[0]-x[1])
        cityA = sum(a for (a,b) in costs[:halfLeng])
        cityB = sum(b for(a,b) in costs[halfLeng:])
        ans = cityA+cityB
        return ans