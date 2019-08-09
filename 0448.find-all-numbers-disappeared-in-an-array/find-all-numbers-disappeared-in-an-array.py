class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numSet = set(nums)
        ans = set(i for i in range(1, len(nums)+1)) - numSet
        ans = list(ans)
        return  ans