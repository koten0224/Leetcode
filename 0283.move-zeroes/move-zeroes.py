class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        index = 0
        leng = len(nums)-1
        while index != leng:
            if not nums[index]:
                count+=1
                leng-=1
                del nums[index]
            else:index+=1
        for _ in range(count):
            nums.append(0)