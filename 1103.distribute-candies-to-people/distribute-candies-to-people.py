class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0 for _ in range(num_people)]
        for i in range(1,10**9):
            index = (i-1) % num_people
            if candies <= i:
                ans[index] += candies
                break
            candies -= i
            ans[index] += i
        return ans