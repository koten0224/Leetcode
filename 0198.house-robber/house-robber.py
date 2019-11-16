class Solution:
    def rob(self, nums: List[int]) -> int:
        leng=len(nums)
        if leng==0:return 0
        if leng<3:return max(nums)
        nums[1]=max(nums[:2])
        for i in range(2,leng):
            nums[i]=max(nums[i-1],nums[i]+nums[i-2])
        return nums[-1]