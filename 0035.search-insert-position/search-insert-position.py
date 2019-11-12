class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index=0
        for i in nums:
            if target<=i:
                return index
            else:index+=1
        return len(nums)