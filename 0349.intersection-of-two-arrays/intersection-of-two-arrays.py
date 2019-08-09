class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        checkSet = set(nums1)
        ans = set()
        for num in nums2:
            if num in checkSet:
                ans.add(num)
        return list(ans)