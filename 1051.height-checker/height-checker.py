class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = 0
        for a,b in zip(heights,sorted(heights)):
            if a != b : ans += 1
        return ans