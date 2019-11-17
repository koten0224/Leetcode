class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic={}
        for i,v in enumerate(numbers):
            p=target-v
            if p in dic:return [dic[p],i+1]
            else:dic[v]=i+1
            