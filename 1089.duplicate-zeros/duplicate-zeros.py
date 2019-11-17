class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        leng=len(arr)
        temp = [i for i,v in enumerate(arr) if not v]
        for i in temp[::-1]:arr.insert(i,0)
        del arr[leng:]