class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1+=nums2
        leng=len(nums1)
        nums1.sort()
        if not leng%2: 
            return (nums1[leng//2]+nums1[leng//2-1])/2
        else:
            return nums1[leng//2]