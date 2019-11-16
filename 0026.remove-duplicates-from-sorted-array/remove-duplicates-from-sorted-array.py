class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = (v for i,v in enumerate(nums) if v!=nums[i-1] or i==0)
        return len(nums)