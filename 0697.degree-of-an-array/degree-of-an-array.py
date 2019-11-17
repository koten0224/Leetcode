from collections import defaultdict
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic=defaultdict(list)
        for i,v in enumerate(nums):
            dic[v].append(i)
        maxmount = max(len(dic[x]) for x in dic)
        return min(x[-1]-x[0]+1 for x in dic.values() if len(x)==maxmount)
        