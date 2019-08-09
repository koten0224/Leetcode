class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in nums1:
            greater=None
            index=nums2.index(i)
            for j in nums2[index+1:]:
                if j>i:
                    greater=j
                    break
            if greater:ans.append(greater)
            else:ans.append(-1)
        
        return ans
            