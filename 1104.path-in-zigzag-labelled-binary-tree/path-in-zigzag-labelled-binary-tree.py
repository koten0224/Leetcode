class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = [label]
        level = int(math.log(label,2))
        stat=level%2
        while level != 0:
            level -= 1
            label//=2
            if level%2!=stat:
                ans.append(label^(2**level-1))
            else:ans.append(label)

        return ans[::-1]
            