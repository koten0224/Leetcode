class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:return [-1,-1]
        leng=len(nums)
        head=0
        tail=leng-1
        index=leng//2
        while 1:
            if nums[index]==target:
                ans=[index]*2
                while ans[0]>-1 and nums[ans[0]]==target:ans[0]-=1
                while ans[1]<leng and nums[ans[1]]==target:ans[1]+=1
                ans[0]+=1
                ans[1]-=1
                return ans
            elif tail-head<=1:break
            elif nums[index]>target:
                tail=index
                index=(head+tail)//2
            elif nums[index]<target:
                head=index
                index=(head+tail)//2
        return [head]*2 if target==nums[head] else([tail]*2 if target==nums[tail] else [-1,-1])