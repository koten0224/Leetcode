class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while nums:
            num=nums[0]
            nums.remove(num)
            if num in nums:nums.remove(num)
            else:return num

        