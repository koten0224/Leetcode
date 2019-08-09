class RecentCounter:

    def __init__(self):
        self.li=[]
    def ping(self, t: int) -> int:
        self.li.append(t)
        while self.li[0]<t-3000:self.li.pop(0)
        return len(self.li)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)