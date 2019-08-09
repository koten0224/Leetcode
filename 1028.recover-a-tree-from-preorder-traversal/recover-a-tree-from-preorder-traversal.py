class Solution:
    def __init__(self):
        self.leftp = '(?<!-)'
        self.dash = '-'
        self.rightp = '(?=\d)'
    def recoverFromPreorder(self, S: str,level=0) -> TreeNode:
        if S.isdigit():return TreeNode(int(S))
        nextLevel = level+1
        patterns = re.split(self.leftp + self.dash * nextLevel + self.rightp , S)
        leng = len(patterns)
        root = TreeNode(int(patterns[0]))
        if leng > 1:
            root.left = self.recoverFromPreorder(patterns[1],nextLevel)
            if leng > 2:
                root.right = self.recoverFromPreorder(patterns[2],nextLevel)
        return root