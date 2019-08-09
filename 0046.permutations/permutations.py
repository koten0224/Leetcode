class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        leng=len(nums)
        def permutation( nums , li = [] ):
            if len(li)==leng:
                ans.append(li)
                return
            index = 0
            for num in nums:
                next_num = nums[:index]+nums[index+1:]
                next_li = li+[num]
                permutation( next_num , next_li )
                index+=1
        permutation(nums)
        return ans
        