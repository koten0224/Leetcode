class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = collections.Counter(arr1)
        Set=set(arr2)
        ans=[i for i in arr2 for _ in range(dic[i])]
        pans=[]
        for i in arr1:
            if i not in Set:pans.append(i)
        return ans+sorted(pans)