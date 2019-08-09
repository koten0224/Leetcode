class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        pre_cnt = 0
        cur_cnt = 1
        N = len(s)
        for i in range(1, N):
            if s[i] == s[i-1]:
                cur_cnt += 1
            else:
                pre_cnt = cur_cnt
                cur_cnt = 1
            if cur_cnt <= pre_cnt:
                res += 1
        return res