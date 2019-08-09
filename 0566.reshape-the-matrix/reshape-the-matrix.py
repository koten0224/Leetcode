class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        x , y=len(nums) , len(nums[0])
        if x*y!=r*c:return nums
        shuffle=[col for row in nums for col in row]
        ans=[ shuffle[i*c:i*c+c] for i in range(r) ]
        return ans